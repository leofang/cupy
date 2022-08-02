#include "../cupy_cub.inl"


namespace cupy {

void cub_device_reduce_prod_CUPY_TYPE_INT64(void* workspace,
                                       size_t& workspace_size,
                                       void* x,
                                       void* y,
                                       int num_items,
                                       cudaStream_t stream) {
#if ( CUPY_TYPE_INT64 != CUPY_TYPE_FLOAT16 )                        \
    || (( CUPY_TYPE_INT64 == CUPY_TYPE_FLOAT16 )                    \
        && ((__CUDA_ARCH__ >= 530 || !defined(__CUDA_ARCH__))  \
            || (defined(__HIPCC__) || defined(CUPY_USE_HIP))))

    _cub_reduce_prod op;
    return dtype_forwarder< int64_t >(op(),
                                         workspace,
                                         workspace_size,
                                         x,
                                         y,
                                         num_items,
                                         stream);

#endif
}

}  // namespace cupy
