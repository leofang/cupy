#ifndef INCLUDE_GUARD_CUPY_CUDNN_H
#define INCLUDE_GUARD_CUPY_CUDNN_H

#ifdef CUPY_USE_HIP

// Since ROCm/HIP does not have cuDNN, we simply include the stubs here
// to avoid code dup.
#include "stub/cupy_cudnn.h"

#elif !defined(CUPY_NO_CUDA)

#include "cuda/cupy_cudnn.h"

#else

#include "stub/cupy_cudnn.h"

#endif // #ifdef CUPY_NO_CUDA

#endif // #ifndef INCLUDE_GUARD_CUPY_CUDNN_H
