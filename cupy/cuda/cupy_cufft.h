// This file is a stub header file of cufft for Read the Docs.

#ifndef INCLUDE_GUARD_CUPY_CUFFT_H
#define INCLUDE_GUARD_CUPY_CUFFT_H

#ifndef CUPY_NO_CUDA
#include <cufft.h>
#include <cufftXt.h>

extern cufftCallbackLoadC CUPY_host_cufft_callback_load_complex64;
extern cufftCallbackLoadZ CUPY_host_cufft_callback_load_complex128;
//cufftCallbackLoadR CUPY_host_cufft_callback_load_float32;
//cufftCallbackLoadD CUPY_host_cufft_callback_load_float64;
extern cufftCallbackStoreC CUPY_host_cufft_callback_store_complex64;
extern cufftCallbackStoreZ CUPY_host_cufft_callback_store_complex128;
//cufftCallbackStoreR CUPY_host_cufft_callback_store_float32;
//cufftCallbackStoreD CUPY_host_cufft_callback_store_float64;

cufftResult setCallbackLoadC(cufftHandle plan, void** callerInfo); 
cufftResult setCallbackLoadZ(cufftHandle plan, void** callerInfo); 
//cufftResult setCallbackLoadR(cufftHandle plan, void** callerInfo); 
//cufftResult setCallbackLoadD(cufftHandle plan, void** callerInfo); 
cufftResult setCallbackStoreC(cufftHandle plan, void** callerInfo);
cufftResult setCallbackStoreZ(cufftHandle plan, void** callerInfo);
//cufftResult setCallbackStoreR(cufftHandle plan, void** callerInfo);
//cufftResult setCallbackStoreD(cufftHandle plan, void** callerInfo);

#else  // CUPY_NO_CUDA
extern "C" {

typedef float cufftReal;
typedef double cufftDoubleReal;

struct cufftComplex{
    float x, y;
};

struct cufftDoubleComplex{
    double x, y;
};

typedef enum {
    CUFFT_SUCCESS = 0,
    CUFFT_INVALID_PLAN = 1,
    CUFFT_ALLOC_FAILED = 2,
    CUFFT_INVALID_TYPE = 3,
    CUFFT_INVALID_VALUE = 4,
    CUFFT_INTERNAL_ERROR = 5,
    CUFFT_EXEC_FAILED = 6,
    CUFFT_SETUP_FAILED = 7,
    CUFFT_INVALID_SIZE = 8,
    CUFFT_UNALIGNED_DATA = 9,
    CUFFT_INCOMPLETE_PARAMETER_LIST = 10,
    CUFFT_INVALID_DEVICE = 11,
    CUFFT_PARSE_ERROR = 12,
    CUFFT_NO_WORKSPACE = 13,
    CUFFT_NOT_IMPLEMENTED = 14,
    CUFFT_LICENSE_ERROR = 15,
    CUFFT_NOT_SUPPORTED = 16,
} cufftResult_t;

typedef int cufftHandle;

typedef enum {} cufftType_t;

// cuFFT Helper Function
cufftResult_t cufftCreate(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftDestroy(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftSetAutoAllocation(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftSetWorkArea(...) {
    return CUFFT_SUCCESS;
}

// cuFFT Stream Function
cufftResult_t cufftSetStream(...) {
    return CUFFT_SUCCESS;
}

// cuFFT Plan Functions
cufftResult_t cufftMakePlan1d(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftMakePlanMany(...) {
    return CUFFT_SUCCESS;
}

// cuFFT Exec Function
cufftResult_t cufftExecC2C(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftExecR2C(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftExecC2R(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftExecZ2Z(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftExecD2Z(...) {
    return CUFFT_SUCCESS;
}

cufftResult_t cufftExecZ2D(...) {
    return CUFFT_SUCCESS;
}

}  // extern "C"

#endif  // CUPY_NO_CUDA

#endif  // INCLUDE_GUARD_CUPY_CUFFT_H
