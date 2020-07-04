#pragma once

#include <cupy/complex/complex.h>

using cupy::thrust::complex;
using cupy::thrust::conj;
using cupy::thrust::real;
using cupy::thrust::imag;
using cupy::thrust::arg;

using cupy::thrust::exp;
using cupy::thrust::log;
using cupy::thrust::log10;
using cupy::thrust::sin;
using cupy::thrust::cos;
using cupy::thrust::tan;
using cupy::thrust::sinh;
using cupy::thrust::cosh;
using cupy::thrust::tanh;
using cupy::thrust::asinh;
using cupy::thrust::acosh;
using cupy::thrust::atanh;
using cupy::thrust::asin;
using cupy::thrust::acos;
using cupy::thrust::atan;

template<typename T>
__host__ __device__ bool isnan(complex<T> x) {
    return isnan(x.real()) || isnan(x.imag());
}

template<typename T>
__host__ __device__ bool isinf(complex<T> x) {
    return isinf(x.real()) || isinf(x.imag());
}

template<typename T>
__host__ __device__ bool isfinite(complex<T> x) {
    return isfinite(x.real()) && isfinite(x.imag());
}

template<typename T>
__host__ __device__ complex<T> log1p(complex<T> x) {
    x += 1;
    return log(x);
}

template<typename T>
__host__ __device__ complex<T> log2(complex<T> x) {
    complex<T> y = log(x);
    y /= log(T(2));
    return y;
}

template<typename T>
__host__ __device__ complex<T> expm1(complex<T> x) {
    complex<T> y = exp(x);
    y -= 1;
    return y;
}

template<typename T>
__host__ __device__ complex<T> min(complex<T> x, complex<T> y) {
    if (isnan(x)) {
        return y;
    } else if (isnan(y)) {
        return x;
    } else if (x.real() < y.real()) {
        return x;
    } else if (x.real() > y.real()) {
        return y;
    } else if (x.imag() < y.imag()) {
        return x;
    } else {
        return y;
    }
}

template<typename T>
__host__ __device__ complex<T> max(complex<T> x, complex<T> y) {
    if (isnan(x)) {
        return y;
    } else if (isnan(y)) {
        return x;
    } else if (x.real() < y.real()) {
        return y;
    } else if (x.real() > y.real()) {
        return x;
    } else if (x.imag() < y.imag()) {
        return y;
    } else {
        return x;
    }
}

template<typename T>
__host__ __device__ complex<T> rint(complex<T> x) {
    return complex<T>(rint(x.real()), rint(x.imag()));
}

// ToDo: assignment operator for complex<T> = T2 for T2 all types
