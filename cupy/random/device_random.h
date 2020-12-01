#ifndef CUPY_DEVICE_RANDOM_H
#define CUPY_DEVICE_RANDOM_H

#ifdef CUPY_NO_CUDA

typedef struct {} curandState;
typedef struct {} curandStateMRG32k3a;
typedef struct {} curandStatePhilox4_32_10_t;
size_t get_curandState_size(...) { return 0; }
size_t get_curandStateMRG32k3a_size(...) { return 0; }
size_t get_curandStatePhilox4_32_10_t_size(...) { return 0; }

#else

size_t get_curandState_size();
size_t get_curandStateMRG32k3a_size();
size_t get_curandStatePhilox4_32_10_t_size();

#endif  // CUPY_NO_CUDA
#endif  // CUPY_DEVICE_RANDOM_H
