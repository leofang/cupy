from cupy.core._reduction import create_reduction_func
from cupy.core.core cimport ndarray

import cupy
if cupy.cuda.cub_enabled:
    from cupy.cuda import cub


cdef ndarray _ndarray_all(ndarray self, axis, out, keepdims):
    if cupy.cuda.cub_enabled:
        dtype = self.dtype
        # result will be None if the reduction is not compatible with CUB
        result = cub.cub_reduction(self, cub.CUPY_CUB_ALL, axis, dtype, out,
                                   keepdims)
        if result is not None:
            return result
    return _all(self, axis=axis, out=out, keepdims=keepdims)


cdef ndarray _ndarray_any(ndarray self, axis, out, keepdims):
    if cupy.cuda.cub_enabled:
        dtype = self.dtype
        # result will be None if the reduction is not compatible with CUB
        result = cub.cub_reduction(self, cub.CUPY_CUB_ANY, axis, dtype, out,
                                   keepdims)
        if result is not None:
            return result
    return _any(self, axis=axis, out=out, keepdims=keepdims)


cdef _all = create_reduction_func(
    'cupy_all',
    ('?->?', 'B->?', 'h->?', 'H->?', 'i->?', 'I->?', 'l->?', 'L->?',
     'q->?', 'Q->?', 'e->?', 'f->?', 'd->?', 'F->?', 'D->?'),
    ('in0 != type_in0_raw(0)', 'a & b', 'out0 = a', 'bool'),
    'true', '')


cdef _any = create_reduction_func(
    'cupy_any',
    ('?->?', 'B->?', 'h->?', 'H->?', 'i->?', 'I->?', 'l->?', 'L->?',
     'q->?', 'Q->?', 'e->?', 'f->?', 'd->?', 'F->?', 'D->?'),
    ('in0 != type_in0_raw(0)', 'a | b', 'out0 = a', 'bool'),
    'false', '')


# Variables to expose to Python
# (cythonized data cannot be exposed to Python, even with cpdef.)


all = _all
any = _any
