#include "device_random.h"

#ifdef CUPY_USE_HIP

#include <hip/hip_runtime.h>
#include <hiprand_kernel.h>
typedef hiprandState curandState;
typedef hiprandStateMRG32k3a curandStateMRG32k3a;
typedef hiprandStatePhilox4_32_10_t curandStatePhilox4_32_10_t;

#elif !defined(CUPY_NO_CUDA)

#include <curand_kernel.h>

#endif

size_t get_curandState_size() {
    return sizeof(curandState);
}

size_t get_curandStateMRG32k3a_size() {
    return sizeof(curandStateMRG32k3a);
}

size_t get_curandStatePhilox4_32_10_t_size() {
    return sizeof(curandStatePhilox4_32_10_t);
}
