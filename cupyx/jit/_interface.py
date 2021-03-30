import collections

import numpy

from cupy_backends.cuda.api import driver
from cupy_backends.cuda.api import runtime
import cupy
from cupy._core import core
from cupyx.jit import _compile
from cupyx.jit import _typerules
from cupyx.jit import _types


class _CudaFunction:
    """JIT cupy function object
    """

    def __init__(self, func, mode, device=False, inline=False):
        self.attributes = []

        if device:
            self.attributes.append('__device__')
        else:
            self.attributes.append('__global__')

        if inline:
            self.attributes.append('inline')

        self.name = getattr(func, 'name', func.__name__)
        self.func = func
        self.mode = mode

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def _emit_code_from_types(self, in_types, ret_type=None):
        return _compile.transpile(
            self.func, self.attributes, self.mode, in_types, ret_type)


class _JitRawKernel:

    def __init__(self, func, mode):
        self._func = func
        self._mode = mode
        self._cache = {}

    def __call__(
            self, grid, block, args, shared_mem=0,
            stream=None, enable_cooperative_groups=False):
        in_types = []
        for x in args:
            if isinstance(x, cupy.ndarray):
                t = _types.CArray.from_ndarray(x)
            elif numpy.isscalar(x):
                t = _typerules.get_ctype_from_scalar(self._mode, x)
            else:
                raise TypeError(f'{type(x)} is not supported for RawKernel')
            in_types.append(t)
        in_types = tuple(in_types)

        kern = self._cache.get(in_types)
        if kern is None:
            result = _compile.transpile(
                self._func,
                ['extern "C"', '__launch_bounds__(256)', '__global__'],
                self._mode,
                in_types,
                _types.Void(),
            )
            fname = result.func_name
            # workaround for hipRTC: as of ROCm 4.1.0 hipRTC still does not
            # recognize "-D", so we have to compile using hipcc...
            backend = 'nvcc' if runtime.is_hip else 'nvrtc'
            print(result.code)
            module = core.compile_with_cache(
                source=result.code,
                options=('-DCUPY_JIT_MODE', '--std=c++11'),
                backend=backend)
            kern = module.get_function(fname)
            self._cache[in_types] = kern
        attr = driver.CU_FUNC_ATTRIBUTE_MAX_DYNAMIC_SHARED_SIZE_BYTES
        print("got it:", driver.funcGetAttribute(attr, kern.ptr))
        driver.funcSetAttribute(kern.ptr, attr, 256)
        print("got it:", driver.funcGetAttribute(attr, kern.ptr))
        #kern(grid, block, args, shared_mem, stream, enable_cooperative_groups)

    def __getitem__(self, grid_and_block):
        grid, block = grid_and_block
        if not isinstance(grid, tuple):
            grid = (grid, 1, 1)
        if not isinstance(block, tuple):
            block = (block, 1, 1)
        return lambda *args, **kwargs: self(grid, block, args, **kwargs)


def rawkernel(mode='cuda'):
    def wrapper(func):
        return _JitRawKernel(func, mode)
    return wrapper


Dim3 = collections.namedtuple('dim3', ['x', 'y', 'z'])


def _create_dim3(name):
    return Dim3(
        _compile.CudaObject(f'{name}.x', _types.uint32),
        _compile.CudaObject(f'{name}.y', _types.uint32),
        _compile.CudaObject(f'{name}.z', _types.uint32),
    )


threadIdx = _create_dim3('threadIdx')
blockDim = _create_dim3('blockDim')
blockIdx = _create_dim3('blockIdx')
gridDim = _create_dim3('gridDim')

syncthreads = _compile.SyncThreads()
shared_memory = _compile.SharedMemory()
