// This file is a stub header file of cuda for Read the Docs.

#ifndef INCLUDE_GUARD_CUPY_COMPLEX_H
#define INCLUDE_GUARD_CUPY_COMPLEX_H

#ifdef CUPY_USE_HIP

#include "hip/cupy_cuComplex.h"

#elif !defined(CUPY_NO_CUDA)

#include "cuda/cupy_cuComplex.h"

#else // #if !defined(CUPY_NO_CUDA) || !defined(CUPY_USE_HIP)

#include "stub/cupy_cuComplex.h"

#endif // #ifndef CUPY_NO_CUDA
#endif // #ifndef INCLUDE_GUARD_CUPY_COMPLEX_H
