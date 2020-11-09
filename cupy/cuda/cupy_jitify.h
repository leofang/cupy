#ifndef INCLUDE_GUARD_CUPY_JITIFY_H
#define INCLUDE_GUARD_CUPY_JITIFY_H

#if !defined(CUPY_NO_CUDA) && !defined(CUPY_USE_HIP)

#include <cupy/jitify/jitify.hpp>

#elif defined(CUPY_USE_HIP)

// At build time, we comment out the includes <cuda.h>, <cuda_runtime.h>, and
// <nvrtc.h> in jitify.hpp, so we supply our CUDA->HIP stubs here
#include <cupy_backends/cuda/cupy_cuda.h>
#include <cupy_backends/cuda/cupy_cuda_runtime.h>
#include <cupy_backends/cuda/cupy_nvrtc.h>

#include <cupy/jitify/jitify.hpp>

#else  // CUPY_NO_CUDA

namespace jitify {
namespace detail {

std::map<std::string, std::string>& get_jitsafe_headers_map();
const int preinclude_jitsafe_headers_count = 0;
const char* preinclude_jitsafe_header_names[] = {};
void load_program(std::string&,
                  std::vector<std::string>&,
                  void*,
                  std::vector<std::string>*,
                  std::map<std::string, std::string>*,
                  std::vector<std::string>*,
                  std::string*);

}  // namespace detail
}  // namespace jitify

#endif

#endif  // INCLUDE_GUARD_CUPY_JITIFY_H
