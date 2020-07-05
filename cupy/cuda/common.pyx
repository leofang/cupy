import numpy


cpdef int _get_dtype_id(dtype) except -1:
    cdef int ret

    if dtype == numpy.int8:
        ret = CUPY_TYPE_INT8
    elif dtype == numpy.uint8:
        ret = CUPY_TYPE_UINT8
    elif dtype == numpy.int16:
        ret = CUPY_TYPE_INT16
    elif dtype == numpy.uint16:
        ret = CUPY_TYPE_UINT16
    elif dtype == numpy.int32:
        ret = CUPY_TYPE_INT32
    elif dtype == numpy.uint32:
        ret = CUPY_TYPE_UINT32
    elif dtype == numpy.int64:
        ret = CUPY_TYPE_INT64
    elif dtype == numpy.uint64:
        ret = CUPY_TYPE_UINT64
    elif dtype == numpy.float16:
        ret = CUPY_TYPE_FLOAT16
    elif dtype == numpy.float32:
        ret = CUPY_TYPE_FLOAT32
    elif dtype == numpy.float64:
        ret = CUPY_TYPE_FLOAT64
    elif dtype == numpy.complex64:
        ret = CUPY_TYPE_COMPLEX64
    elif dtype == numpy.complex128:
        ret = CUPY_TYPE_COMPLEX128
    elif dtype == numpy.bool:
        ret = CUPY_TYPE_BOOL
    else:
        raise ValueError('Unsupported dtype ({})'.format(dtype))
    return ret
