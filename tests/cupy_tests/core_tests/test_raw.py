import pytest
import unittest

import cupy


_test_source1 = r'''
extern "C" __global__
void test_sum(const float* x1, const float* x2, float* y) {
    int tid = blockDim.x * blockIdx.x + threadIdx.x;
    y[tid] = x1[tid] + x2[tid];
}
'''

# test compiling and invoking multiple kernels in one single .cubin
_test_source2 = r'''
extern "C"{

__global__ void test_sum(const float* x1, const float* x2, float* y, \
                         unsigned int N)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;
    if (tid < N)
    {
        y[tid] = x1[tid] + x2[tid];
    }
}

__global__ void test_multiply(const float* x1, const float* x2, float* y, \
                              unsigned int N)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;
    if (tid < N)
    {
        y[tid] = x1[tid] * x2[tid];
    }
}

}
'''

# test C macros
_test_source3 = r'''
#ifndef PRECISION
    #define PRECISION 2
#endif

#if PRECISION == 2
    #define TYPE double
#elif PRECISION == 1
    #define TYPE float
#else
    #error precision not supported
#endif

extern "C"{

__global__ void test_sum(const TYPE* x1, const TYPE* x2, TYPE* y, \
                         unsigned int N)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;
    if (tid < N)
    {
        y[tid] = x1[tid] + x2[tid];
    }
}

__global__ void test_multiply(const TYPE* x1, const TYPE* x2, TYPE* y, \
                              unsigned int N)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;
    if (tid < N)
    {
        y[tid] = x1[tid] * x2[tid];
    }
}

}
'''

_test_source5 = r'''
extern "C"{

__global__ void test_kernel_inner(float *arr, int N)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;
    unsigned int inner_blk = 2;
    unsigned int inner_len = inner_blk*sizeof(float);

    if (tid < N)
        arr[tid] = 1.0;
}

__global__ void test_kernel(float *arr, int N, int inner_blk)
{
    unsigned int tid = blockDim.x * blockIdx.x + threadIdx.x;

    if (tid < N/inner_blk)
        test_kernel_inner<<<inner_blk, 1>>>(arr+tid*inner_blk, inner_blk);
}

}
'''


class TestRaw(unittest.TestCase):

    def setUp(self):
        self.kern = cupy.RawKernel(_test_source1, 'test_sum')
        self.mod2 = cupy.RawModule(_test_source2)
        self.mod3 = cupy.RawModule(_test_source3, ("-DPRECISION=2",))

    def _helper(self, kernel, dtype):
        N = 10
        x1 = cupy.arange(N**2, dtype=dtype).reshape(N, N)
        x2 = cupy.ones((N, N), dtype=dtype)
        y = cupy.zeros((N, N), dtype=dtype)
        kernel((N,), (N,), (x1, x2, y, N**2))
        return x1, x2, y

    def test_basic(self):
        x1, x2, y = self._helper(self.kern, cupy.float32)
        assert cupy.allclose(y, x1 + x2)

    def test_kernel_attributes(self):
        attrs = self.kern.attributes
        for attribute in ['binary_version',
                          'cache_mode_ca',
                          'const_size_bytes',
                          'local_size_bytes',
                          'max_dynamic_shared_size_bytes',
                          'max_threads_per_block',
                          'num_regs',
                          'preferred_shared_memory_carveout',
                          'ptx_version',
                          'shared_size_bytes']:
            assert attribute in attrs
        assert self.kern.num_regs > 0
        assert self.kern.max_threads_per_block > 0
        assert self.kern.shared_size_bytes == 0

    def test_module(self):
        module = self.mod2
        ker_sum = module.get_function('test_sum')
        ker_times = module.get_function('test_multiply')

        x1, x2, y = self._helper(ker_sum, cupy.float32)
        assert cupy.allclose(y, x1 + x2)

        x1, x2, y = self._helper(ker_times, cupy.float32)
        assert cupy.allclose(y, x1 * x2)

    def test_compiler_flag(self):
        module = self.mod3
        ker_sum = module.get_function('test_sum')
        ker_times = module.get_function('test_multiply')

        x1, x2, y = self._helper(ker_sum, cupy.float64)
        assert cupy.allclose(y, x1 + x2)

        x1, x2, y = self._helper(ker_times, cupy.float64)
        assert cupy.allclose(y, x1 * x2)

    def test_invalid_compiler_flag(self):
        with pytest.raises(cupy.cuda.compiler.CompileException) as ex:
            cupy.RawModule(_test_source3, ("-DPRECISION=3",))
        assert 'precision not supported' in str(ex.value)

    def test_module_load_failure(self):
        # in principle this test is better done in test_driver.py, but
        # this error is more likely to appear when using RawModule, so
        # let us do it here
        import os
        with pytest.raises(cupy.cuda.driver.CUDADriverError) as ex:
            cupy.RawModule(os.path.expanduser("~/this_does_not_exist.cubin"))
        assert 'CUDA_ERROR_FILE_NOT_FOUND' in str(ex.value)

    def test_get_function_failure(self):
        # in principle this test is better done in test_driver.py, but
        # this error is more likely to appear when using RawModule, so
        # let us do it here
        with pytest.raises(cupy.cuda.driver.CUDADriverError) as ex:
            self.mod2.get_function("no_such_kernel")
        assert 'CUDA_ERROR_NOT_FOUND' in str(ex.value)

    def test_dynamical_parallelism(self):
        ker = cupy.RawKernel(_test_source5, 'test_kernel', options=('-dc',))
        N = 15
        inner_chunk = 3
        x = cupy.zeros((N,), dtype=cupy.float32)
        ker((1,), (N,), (x, N, inner_chunk))
        assert (x == 1.0).all()

    def test_dynamical_parallelism_compile_failure(self):
        ker = cupy.RawKernel(_test_source5, 'test_kernel',)
        N = 15
        inner_chunk = 3
        x = cupy.zeros((N,), dtype=cupy.float32)
        with pytest.raises(cupy.cuda.driver.CUDADriverError) as ex:
            ker((1,), (N,), (x, N, inner_chunk))
