#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <cufft.h>
#include <cufftXt.h>
#include <cuda_runtime.h>
#define checkCudaErrors(x) {assert (0==x);}


int main() {
    int nGPUs = 2;
    int whichGPUs[] = {0, 1};

    // start and end from device 0
    // when we start a fresh program, the peer access is disabled by default
    // (we check the peer access status by trial and error)
    printf("before creating a plan...\n");
    checkCudaErrors(cudaSetDevice(0));
    for (int i=0; i<2; i++) {
        cudaSetDevice(i);
	cudaError_t status = cudaDeviceDisablePeerAccess((i+1)%2);
        if (status != cudaErrorPeerAccessNotEnabled) {
            printf("dev: %i, status: %s\n", i, cudaGetErrorString(status));
	    exit(-1);
        }
    }
    checkCudaErrors(cudaSetDevice(0));

    // cufftCreate() - Create an empty plan
    cufftResult result;
    cufftHandle plan_input;
    checkCudaErrors (cufftCreate (&plan_input));

    // cufftXtSetGPUs() - Define which GPUs to use
    result = cufftXtSetGPUs (plan_input, nGPUs, whichGPUs);
    if (result != CUFFT_SUCCESS)
    {
        printf ("cufftXtSetGPUs failed\n"); exit (EXIT_FAILURE);
	exit(-1);
    }

    int new_size = 128;
    size_t* worksize;
    worksize =(size_t*)malloc(sizeof(size_t) * nGPUs);

    // cufftMakePlan1d() - Create the plan
    checkCudaErrors(cufftMakePlan1d(plan_input, new_size, CUFFT_C2C, 1, worksize));

    // start and end from device 0
    // cuFFT internally enabled bidirectional access upon this point
    printf("after creating a plan/before destroying it...\n");
    checkCudaErrors(cudaSetDevice(0));
    for (int i=0; i<2; i++) {
        cudaSetDevice(i);
	cudaError_t status = cudaDeviceEnablePeerAccess((i+1)%2, 0);
        if (status != cudaErrorPeerAccessAlreadyEnabled) {
            printf("dev: %i, status: %s\n", i, cudaGetErrorString(status));
	    exit(-1);
        }
    }
    checkCudaErrors(cudaSetDevice(0));

    // cufftDestroy() - Destroy FFT plan
    checkCudaErrors(cufftDestroy(plan_input));

    // start and end from device 0
    // cuFFT only disabled 1->0 access, but not 0->1 access, so we error out at i=1
    printf("after destroying the plan...\n");
    checkCudaErrors(cudaSetDevice(0));
    for (int i=0; i<2; i++) {
        cudaSetDevice(i);
	cudaError_t status = cudaDeviceDisablePeerAccess((i+1)%2);
        if (status != cudaErrorPeerAccessNotEnabled) {
            printf("dev: %i, status: %s\n", i, cudaGetErrorString(status));
	    exit(-1);
        }
    }
    checkCudaErrors(cudaSetDevice(0));

    free(worksize);

    return 0;
}
