import pickle
import unittest

import numpy

from cupy import testing
from cupy.cuda import cufft
from cupy.fft import config
from cupy.fft.fft import _convert_fft_type

from ..fft_tests.test_fft import multi_gpu_config


class TestExceptionPicklable(unittest.TestCase):

    def test(self):
        e1 = cufft.CuFFTError(1)
        e2 = pickle.loads(pickle.dumps(e1))
        assert e1.args == e2.args
        assert str(e1) == str(e2)


# This class tests multi-GPU Plan1d with data sitting on host.
# Internally, we use cuFFT's data transfer API to ensure the
# data is in order.

@testing.parameterize(*testing.product({
    'shape': [(64,), (4, 16), (128,), (8, 32)],
}))
@testing.multi_gpu(2)
class TestMultiGpuPlan1dNumPy(unittest.TestCase):

    @multi_gpu_config(gpu_configs=[[0, 1], [1, 0]])
    @testing.for_complex_dtypes()
    def test_fft(self, dtype):
        a = testing.shaped_random(self.shape, numpy, dtype)

        if len(self.shape) == 1:
            batch = 1
            nx = self.shape[0]
        elif len(self.shape) == 2:
            batch = self.shape[0]
            nx = self.shape[1]

        # compute via cuFFT
        cufft_type = _convert_fft_type(a.dtype, 'C2C')
        plan = cufft.Plan1d(nx, cufft_type, batch, devices=config._devices)
        out_cp = numpy.empty_like(a)
        plan.fft(a, out_cp, cufft.CUFFT_FORWARD)

        out_np = numpy.fft.fft(a)
        # np.fft.fft alway returns np.complex128
        if dtype is numpy.complex64:
            out_np = out_np.astype(dtype)

        assert numpy.allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)

        # compute it again to ensure Plan1d's internal state is reset
        plan.fft(a, out_cp, cufft.CUFFT_FORWARD)

        assert numpy.allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)

    @multi_gpu_config(gpu_configs=[[0, 1], [1, 0]])
    @testing.for_complex_dtypes()
    def test_ifft(self, dtype):
        a = testing.shaped_random(self.shape, numpy, dtype)

        if len(self.shape) == 1:
            batch = 1
            nx = self.shape[0]
        elif len(self.shape) == 2:
            batch = self.shape[0]
            nx = self.shape[1]

        # compute via cuFFT
        cufft_type = _convert_fft_type(a.dtype, 'C2C')
        plan = cufft.Plan1d(nx, cufft_type, batch, devices=config._devices)
        out_cp = numpy.empty_like(a)
        plan.fft(a, out_cp, cufft.CUFFT_INVERSE)
        # normalization
        out_cp /= nx

        out_np = numpy.fft.ifft(a)
        # np.fft.fft alway returns np.complex128
        if dtype is numpy.complex64:
            out_np = out_np.astype(dtype)

        assert numpy.allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)

        # compute it again to ensure Plan1d's internal state is reset
        plan.fft(a, out_cp, cufft.CUFFT_INVERSE)
        # normalization
        out_cp /= nx

        assert numpy.allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)

    @multi_gpu_config(gpu_configs=[[0, 1], [1, 0]])
    #@testing.for_float_dtypes(no_float16=True)
    #def test_rfft(self, dtype):
    def test_rfft(self):
        dtype = numpy.float64
        #a = testing.shaped_random(self.shape, numpy, dtype)
        a = numpy.arange(4*16, dtype=dtype).reshape(4, 16)

        if len(self.shape) == 1:
            self.skipTest('batch = 1 is not supported')
        elif len(self.shape) == 2:
            batch = self.shape[0]
            nx = self.shape[1]
        if dtype == numpy.float32:
            out_dtype = numpy.complex64
        elif dtype == numpy.float64:
            out_dtype = numpy.complex128
        else:
            raise ValueError

        # compute via cuFFT
        cufft_type = _convert_fft_type(a.dtype, 'R2C')
        plan = cufft.Plan1d(nx, cufft_type, batch, devices=config._devices)
        #plan = cufft.Plan1d(nx, cufft_type, batch)
        import cupy
        print(nx, cufft_type, batch)
        print(a.shape, a.dtype, a, '\n')
        out_cp = numpy.zeros((batch, nx // 2 + 1), dtype=out_dtype)
        print(out_cp.shape, out_cp.dtype, out_cp, '\n')
        plan.fft(a, out_cp)
        print('finished:', out_cp.shape, out_cp.dtype, out_cp, '\n')

        # compute via numpy
        out_np = numpy.fft.rfft(a)
        print(out_np.shape, out_np.dtype, out_np, '\n')

        numpy.testing.assert_allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)

        # compute it again to ensure Plan1d's internal state is reset
        out_cp = numpy.empty((batch, nx // 2 + 1), dtype=out_dtype)
        plan.fft(a, out_cp)

        numpy.testing.assert_allclose(out_cp, out_np, rtol=1e-4, atol=1e-7)
