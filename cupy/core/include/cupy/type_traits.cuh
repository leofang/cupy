// Implements a casting function to make it compatible with scipy
// Use like cast<to_type>(value)
// It's actually really simple - most of this is <type_traits>
// Small bit of <type_traits> which cannot be imported in NVRTC
// Requires compiling with --std=c++11 or higher
// Author: Jeffrey Bush (@coderforlife)

// TODO(leofang): integrate with jitify support (#3408)
template<bool B, class T=void> struct enable_if {};
template<class T> struct enable_if<true, T> { typedef T type; };
template<class T> struct remove_const          { typedef T type; };
template<class T> struct remove_const<const T> { typedef T type; };
template<class T> struct remove_volatile             { typedef T type; };
template<class T> struct remove_volatile<volatile T> { typedef T type; };
template<class T> struct remove_cv {
  typedef typename remove_volatile<typename remove_const<T>::type>::type type;
};
template<class T, T v>
struct integral_constant { static constexpr T value = v; };
//struct true_type { static constexpr bool value = true; };
//struct false_type { static constexpr bool value = false; };
typedef integral_constant<bool, true> true_type;
typedef integral_constant<bool, false> false_type;
template<class T> struct __is_fp : public false_type {};
template<>        struct __is_fp<float> : public true_type {};
template<>        struct __is_fp<double> : public true_type {};
template<>        struct __is_fp<long double> : public true_type {};
template<class T> struct is_floating_point
    : public __is_fp<typename remove_cv<T>::type> {};
template<class T> struct is_signed : integral_constant<bool, (T)(-1)<0> {};
template <typename B, typename A>
__device__
typename enable_if<!is_floating_point<A>::value||is_signed<B>::value, B>::type
cast(A a) { return (B)a; }
template <typename B, typename A>
__device__
typename enable_if<is_floating_point<A>::value&&!is_signed<B>::value, B>::type
cast(A a) { return (a >= 0) ? (B)a : -(B)(-a); }
