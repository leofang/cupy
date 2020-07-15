#pragma once
#ifdef CUPY_CUB_BLOCK_REDUCTION
#include <cupy/complex.cuh>
#endif


// math
#ifndef M_PI
#define M_PI 3.1415926535897932384626433832795
#endif

#ifdef __HIPCC__

#include <hip/hip_fp16.h>

#elif __CUDACC_VER_MAJOR__ >= 9

#include <cuda_fp16.h>

#else  // #if __CUDACC_VER_MAJOR__ >= 9

struct __half_raw {
  unsigned short x;
};

struct half {
private:
  unsigned short data_;
public:
  __device__ half() {}
  __device__ half(const half &v) : data_(v.data_) {}
  __device__ half(float v) : data_(__float2half_rn(v)) {}

  explicit __device__ half(const __half_raw &v) : data_(v.x) {}
  explicit __device__ half(bool v) : data_(__float2half_rn(float(v))) {}
  explicit __device__ half(double v) : data_(__float2half_rn(float(v))) {}
  explicit __device__ half(int v) : data_(__float2half_rn(float(v))) {}
  explicit __device__ half(unsigned int v) : data_(__float2half_rn(float(v))) {}
  explicit __device__ half(long long v) : data_(__float2half_rn(float(v))) {}
  explicit __device__ half(unsigned long long v) : data_(__float2half_rn(float(v))) {}

  __device__ operator float() const {return __half2float(data_);}
  __device__ operator __half_raw() const {__half_raw ret = {data_}; return ret;}
};

#endif  // #if __CUDACC_VER_MAJOR__ >= 9


class float16 {
private:
  half  data_;
public:
  __device__ float16() {}
  __device__ float16(float v) : data_(v) {}

  explicit __device__ float16(bool v) : data_(float(v)) {}
  explicit __device__ float16(double v) : data_(v) {}
  explicit __device__ float16(int v) : data_(v) {}
  explicit __device__ float16(unsigned int v) : data_(v) {}
  explicit __device__ float16(long long v) : data_(v) {}
  explicit __device__ float16(unsigned long long v) : data_(v) {}

  explicit __device__ float16(const half &v): data_(v) {}
  explicit __device__ float16(const __half_raw &v): data_(v) {}

  __device__ operator float() const {return float(data_);}
#ifdef CUPY_CUB_BLOCK_REDUCTION
  // these type conversion functions are needed for CUB load to be able
  // to do an implicit conversion
  __device__ operator complex<float>() const {
      return complex<float>(float(data_), 0);
  }
  __device__ operator complex<double>() const {
      return complex<double>(double(data_), 0);
  }
#endif

  static const unsigned short nan = 0x7e00u;

  __device__ int iszero() const {
    return (__half_raw(data_).x & 0x7fffu) == 0;
  }

  __device__ int isnan() const {
    __half_raw raw_ = __half_raw(data_);
    return (raw_.x & 0x7c00u) == 0x7c00u && (raw_.x & 0x03ffu) != 0x0000u;
  }

  __device__ int isinf() const {
    return (__half_raw(data_).x & 0x7fffu) == 0x7c00u;
  }

  __device__ int isfinite() const {
    return (__half_raw(data_).x & 0x7c00u) != 0x7c00u;
  }

  __device__ int signbit() const {
    return (__half_raw(data_).x & 0x8000u) != 0;
  }

  template<typename T>
  inline __device__ float16& operator+=(const T& rhs) {
    *this = *this + rhs;
    return *this;
  }

  template<typename T>
  inline __device__ float16& operator-=(const T& rhs) {
    *this = *this - rhs;
    return *this;
  }

  template<typename T>
  inline __device__ float16& operator*=(const T& rhs) {
    *this = *this * rhs;
    return *this;
  }

  template<typename T>
  inline __device__ float16& operator/=(const T& rhs) {
    *this = *this / rhs;
    return *this;
  }

  friend __device__ float16 copysign(float16 x, float16 y) {
    __half_raw x_raw_ = __half_raw(x.data_);
    __half_raw y_raw_ = __half_raw(y.data_);
    __half_raw ret_raw_;
    ret_raw_.x = (x_raw_.x & 0x7fffu) | (y_raw_.x & 0x8000u);
    return float16(ret_raw_);
  }

  friend __device__ float16 nextafter(float16 x, float16 y) {
    __half_raw x_raw_ = __half_raw(x.data_);
    __half_raw y_raw_ = __half_raw(y.data_);
    __half_raw ret_raw_;
    if (!x.isfinite() || y.isnan()) {
      ret_raw_.x = nan;
    } else if (eq_nonan(x, y)) {
      ret_raw_.x = x_raw_.x;
    } else if (x.iszero()) {
      ret_raw_.x = (y_raw_.x & 0x8000u) + 1;
    } else if (!(x_raw_.x & 0x8000u)) {
      if (static_cast<signed short>(x_raw_.x) > static_cast<signed short>(y_raw_.x)) {
        ret_raw_.x = x_raw_.x - 1;
      } else {
        ret_raw_.x = x_raw_.x + 1;
      }
    } else if(!(y_raw_.x & 0x8000u) || (x_raw_.x & 0x7fffu) > (y_raw_.x & 0x7fffu)) {
      ret_raw_.x = x_raw_.x - 1;
    } else {
      ret_raw_.x = x_raw_.x + 1;
    }
    return float16(ret_raw_);
  }

private:
  static __device__ int eq_nonan(const float16 x, const float16 y) {
    __half_raw x_raw_ = __half_raw(x.data_);
    __half_raw y_raw_ = __half_raw(y.data_);
    return (x_raw_.x == y_raw_.x || ((x_raw_.x | y_raw_.x) & 0x7fff) == 0);
  }
};


__device__ float16 min(float16 x, float16 y) {
  return float16(min(float(x), float(y)));
}
__device__ float16 max(float16 x, float16 y) {
  return float16(max(float(x), float(y)));
}
__device__ float16 fmin(float16 x, float16 y) {
  return float16(fmin(float(x), float(y)));
}
__device__ float16 fmax(float16 x, float16 y) {
  return float16(fmax(float(x), float(y)));
}
__device__ int iszero(float16 x) {return x.iszero();}
__device__ int isnan(float16 x) {return x.isnan();}
__device__ int isinf(float16 x) {return x.isinf();}
__device__ int isfinite(float16 x) {return x.isfinite();}
__device__ int signbit(float16 x) {return x.signbit();}
