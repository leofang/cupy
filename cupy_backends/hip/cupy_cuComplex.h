#ifndef INCLUDE_GUARD_CUPY_HIP_COMPLEX_H
#define INCLUDE_GUARD_CUPY_HIP_COMPLEX_H

extern "C" {

///////////////////////////////////////////////////////////////////////////////
// cuComplex.h
///////////////////////////////////////////////////////////////////////////////

struct cuComplex{
    float x, y;
};

struct cuDoubleComplex{
    double x, y;
};

} // extern "C"

#endif // #ifndef CUPY_NO_CUDA
#endif // #ifndef INCLUDE_GUARD_HIP_CUPY_COMPLEX_H
