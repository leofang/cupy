cdef extern from *:
    ctypedef float Float 'cufftReal'
    ctypedef double Double 'cufftDoubleReal'
    ctypedef int Result 'cufftResult_t'
    ctypedef int Handle 'cufftHandle'
    ctypedef int Type 'cufftType_t'
    ctypedef int CallbackType 'cufftXtCallbackType'


cpdef enum:
    CUFFT_C2C = 0x29
    CUFFT_R2C = 0x2a
    CUFFT_C2R = 0x2c
    CUFFT_Z2Z = 0x69
    CUFFT_D2Z = 0x6a
    CUFFT_Z2D = 0x6c

    CUFFT_FORWARD = -1
    CUFFT_INVERSE = 1

    CUFFT_CB_LD_COMPLEX = 0x0
    CUFFT_CB_LD_COMPLEX_DOUBLE = 0x1
    CUFFT_CB_LD_REAL = 0x2
    CUFFT_CB_LD_REAL_DOUBLE = 0x3
    CUFFT_CB_ST_COMPLEX = 0x4
    CUFFT_CB_ST_COMPLEX_DOUBLE = 0x5
    CUFFT_CB_ST_REAL = 0x6
    CUFFT_CB_ST_REAL_DOUBLE = 0x7
    CUFFT_CB_UNDEFINED = 0x8


cpdef get_current_plan()
