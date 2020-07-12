/*
 * Small bit of <type_traits> which cannot be included in NVRTC
 *
 * Originally by: Jeffrey Bush (@coderforlife)
 */
// TODO(leofang): integrate with jitify support (#3408)

#pragma once
#include <cupy/float16.cuh>


// _MSVC_LANG is only defined in MSVC 2015U3+.
#if __cplusplus >= 201103L \
    || (defined(_MSVC_LANG) && _MSVC_LANG >= 201103L)  // C++11 support
#define CUPY_CPP11_SUPPORTED 1
#else
#define CUPY_CPP11_SUPPORTED 0
#endif

// wrap with namespaces to avoid name clash
namespace cupy {
namespace detail {

template<bool B, class T=void> struct enable_if {};
template<class T> struct enable_if<true, T> { typedef T type; };
template<class T> struct remove_const          { typedef T type; };
template<class T> struct remove_const<const T> { typedef T type; };
template<class T> struct remove_volatile             { typedef T type; };
template<class T> struct remove_volatile<volatile T> { typedef T type; };
template<class T> struct remove_cv {
  typedef typename remove_volatile<typename remove_const<T>::type>::type type;
};

template<class T, T v> struct integral_constant {
    #if CUPY_CPP11_SUPPORTED
    static constexpr T value = v;
    #else
    static const T value = v;
    #endif
};
typedef integral_constant<bool, true> true_type;
typedef integral_constant<bool, false> false_type;

template<class T> struct __is_fp : public false_type {};
template<>        struct __is_fp<float> : public true_type {};
template<>        struct __is_fp<double> : public true_type {};
template<>        struct __is_fp<long double> : public true_type {};
template<>        struct __is_fp<cupy::float16> : public true_type {};
template<class T>
struct is_floating_point : public __is_fp<typename remove_cv<T>::type> {};

// a checker for isolating fp16; no counterpart in C++ standard
template<class T> struct __is_fp16 : public false_type {};
template<>        struct __is_fp16<cupy::float16> : public true_type {};
template<class T>
struct is_fp16 : public __is_fp16<typename remove_cv<T>::type> {};

template<class T>
struct is_signed : integral_constant<bool, (T)(-1)<0> {};

}  // namespace detail
}  // namespace cupy
