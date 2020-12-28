#ifndef _CUPY_TEST_H
#define _CUPY_TEST_H


// This enum holds the generators, we can't fully templatize the generators
// because the dynamic design of BitGenerators in the python side does not allow us
// to determine the correct type at compile time
enum RandGenerators{
   CURAND_XOR_WOW,
   CURAND_MRG32k3a,
   CURAND_PHILOX_4x32_10
};

// forward declaration for CUDA/HIP/RTD
void init_curand_generator(int generator, intptr_t state_ptr, uint64_t seed, ssize_t size, intptr_t stream);
void raw(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream);
void interval_32(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, int32_t mx, int32_t mask);
void interval_64(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, int64_t mx, int64_t mask);
void beta(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, double a, double b);
void exponential(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream);
size_t get_curandState_size();
size_t get_curandStateMRG32k3a_size();
size_t get_curandStatePhilox4_32_10_t_size();

#if !defined(CUPY_USE_HIP) && defined(CUPY_NO_CUDA)

typedef struct {} curandState;
typedef struct {} curandStateMRG32k3a;
typedef struct {} curandStatePhilox4_32_10_t;

//Travis doesn't like variadic templates in these functions
void init_curand_generator(int generator, intptr_t state_ptr, uint64_t seed, ssize_t size, intptr_t stream) {}
void raw(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream) {}
void interval_32(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, int32_t mx, int32_t mask) {}
void interval_64(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, int64_t mx, int64_t mask) {}
void beta(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream, double a, double b) {}
void exponential(int generator, intptr_t state, intptr_t out, ssize_t size, intptr_t stream) {}

size_t get_curandState_size(...) { return 0; }
size_t get_curandStateMRG32k3a_size(...) { return 0; }
size_t get_curandStatePhilox4_32_10_t_size(...) { return 0; }
#endif
#endif
