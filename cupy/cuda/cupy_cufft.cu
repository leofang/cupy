#include "cupy_cufft.h"


//extern __device__ cufftCallbackLoadC CUPY_device_cufft_callback_load_complex64;
//extern __device__ cufftCallbackLoadZ CUPY_device_cufft_callback_load_complex128;
//extern __device__ cufftCallbackLoadR CUPY_device_cufft_callback_load_float32;
//extern __device__ cufftCallbackLoadD CUPY_device_cufft_callback_load_float64;
//extern __device__ cufftCallbackStoreC CUPY_device_cufft_callback_store_complex64;
//extern __device__ cufftCallbackStoreZ CUPY_device_cufft_callback_store_complex128;
//extern __device__ cufftCallbackStoreR CUPY_device_cufft_callback_store_float32;
//extern __device__ cufftCallbackStoreD CUPY_device_cufft_callback_store_float64;


cufftResult setCallbackLoadC(cufftHandle plan, void** callerInfo) {
    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_load_complex64, CUFFT_CB_LD_COMPLEX, callerInfo);
}

cufftResult setCallbackLoadZ(cufftHandle plan, void** callerInfo) {
    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_load_complex128, CUFFT_CB_LD_COMPLEX_DOUBLE, callerInfo);
}

//cufftResult setCallbackLoadR(cufftHandle plan, void** callerInfo) {
//    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_load_float32, CUFFT_CB_LD_REAL, callerInfo);
//}
//
//cufftResult setCallbackLoadD(cufftHandle plan, void** callerInfo) {
//    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_load_float64, CUFFT_CB_LD_REAL_DOUBLE, callerInfo);
//}

cufftResult setCallbackStoreC(cufftHandle plan, void** callerInfo) {
    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_store_complex64, CUFFT_CB_ST_COMPLEX, callerInfo);
}

cufftResult setCallbackStoreZ(cufftHandle plan, void** callerInfo) {
    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_store_complex128, CUFFT_CB_ST_COMPLEX_DOUBLE, callerInfo);
}

//cufftResult setCallbackStoreR(cufftHandle plan, void** callerInfo) {
//    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_store_float32, CUFFT_CB_ST_REAL, callerInfo);
//}
//
//cufftResult setCallbackStoreD(cufftHandle plan, void** callerInfo) {
//    return cufftXtSetCallback(plan, (void**)&CUPY_host_cufft_callback_store_float64, CUFFT_CB_ST_REAL_DOUBLE, callerInfo);
//}
