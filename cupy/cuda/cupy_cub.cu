#include "cupy_cub.h"  // need to make atomicAdd visible to CUB templates early
#include <cupy/type_dispatcher.cuh>


namespace cupy {



}  // namespace cupy



//
// APIs exposed to CuPy
//

/* -------- device reduce -------- */

void cub_device_reduce(void* workspace, size_t& workspace_size, void* x, void* y,
    int num_items, cudaStream_t stream, int op, int dtype_id)
{
    switch(op) {
    case CUPY_CUB_SUM:      return dtype_dispatcher(dtype_id, _cub_reduce_sum(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_MIN:      return dtype_dispatcher(dtype_id, _cub_reduce_min(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_MAX:      return dtype_dispatcher(dtype_id, _cub_reduce_max(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_ARGMIN:   return dtype_dispatcher(dtype_id, _cub_reduce_argmin(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_ARGMAX:   return dtype_dispatcher(dtype_id, _cub_reduce_argmax(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_PROD:     return dtype_dispatcher(dtype_id, _cub_reduce_prod(),
                                workspace, workspace_size, x, y, num_items, stream);
    default:            throw std::runtime_error("Unsupported operation");
    }
}

size_t cub_device_reduce_get_workspace_size(void* x, void* y, int num_items,
    cudaStream_t stream, int op, int dtype_id)
{
    size_t workspace_size = 0;
    cub_device_reduce(NULL, workspace_size, x, y, num_items, stream,
                      op, dtype_id);
    return workspace_size;
}

/* -------- device segmented reduce -------- */

void cub_device_segmented_reduce(void* workspace, size_t& workspace_size,
    void* x, void* y, int num_segments, int segment_size,
    cudaStream_t stream, int op, int dtype_id)
{
    // CUB internally use int for offset...
    // This iterates over [0, segment_size, 2*segment_size, 3*segment_size, ...]
    #ifndef CUPY_USE_HIP
    CountingInputIterator<int> count_itr(0);
    #else
    rocprim::counting_iterator<int> count_itr(0);
    #endif
    _arange scaling(segment_size);
    seg_offset_itr itr(count_itr, scaling);

    switch(op) {
    case CUPY_CUB_SUM:
        return dtype_dispatcher(dtype_id, _cub_segmented_reduce_sum(),
                   workspace, workspace_size, x, y, num_segments, itr, stream);
    case CUPY_CUB_MIN:
        return dtype_dispatcher(dtype_id, _cub_segmented_reduce_min(),
                   workspace, workspace_size, x, y, num_segments, itr, stream);
    case CUPY_CUB_MAX:
        return dtype_dispatcher(dtype_id, _cub_segmented_reduce_max(),
                   workspace, workspace_size, x, y, num_segments, itr, stream);
    case CUPY_CUB_PROD:
        return dtype_dispatcher(dtype_id, _cub_segmented_reduce_prod(),
                   workspace, workspace_size, x, y, num_segments, itr, stream);
    default:
        throw std::runtime_error("Unsupported operation");
    }
}

size_t cub_device_segmented_reduce_get_workspace_size(void* x, void* y,
    int num_segments, int segment_size,
    cudaStream_t stream, int op, int dtype_id)
{
    size_t workspace_size = 0;
    cub_device_segmented_reduce(NULL, workspace_size, x, y,
                                num_segments, segment_size, stream,
                                op, dtype_id);
    return workspace_size;
}

/*--------- device spmv (sparse-matrix dense-vector multiply) ---------*/

void cub_device_spmv(void* workspace, size_t& workspace_size, void* values,
    void* row_offsets, void* column_indices, void* x, void* y, int num_rows,
    int num_cols, int num_nonzeros, cudaStream_t stream,
    int dtype_id)
{
    #ifndef CUPY_USE_HIP
    return dtype_dispatcher(dtype_id, _cub_device_spmv(),
                            workspace, workspace_size, values, row_offsets,
                            column_indices, x, y, num_rows, num_cols,
                            num_nonzeros, stream);
    #endif
}

size_t cub_device_spmv_get_workspace_size(void* values, void* row_offsets,
    void* column_indices, void* x, void* y, int num_rows, int num_cols,
    int num_nonzeros, cudaStream_t stream, int dtype_id)
{
    size_t workspace_size = 0;
    #ifndef CUPY_USE_HIP
    cub_device_spmv(NULL, workspace_size, values, row_offsets, column_indices,
                    x, y, num_rows, num_cols, num_nonzeros, stream, dtype_id);
    #endif
    return workspace_size;
}

/* -------- device scan -------- */

void cub_device_scan(void* workspace, size_t& workspace_size, void* x, void* y,
    int num_items, cudaStream_t stream, int op, int dtype_id)
{
    switch(op) {
    case CUPY_CUB_CUMSUM:
        return dtype_dispatcher(dtype_id, _cub_inclusive_sum(),
                                workspace, workspace_size, x, y, num_items, stream);
    case CUPY_CUB_CUMPROD:
        return dtype_dispatcher(dtype_id, _cub_inclusive_product(),
                                workspace, workspace_size, x, y, num_items, stream);
    default:
        throw std::runtime_error("Unsupported operation");
    }
}

size_t cub_device_scan_get_workspace_size(void* x, void* y, int num_items,
    cudaStream_t stream, int op, int dtype_id)
{
    size_t workspace_size = 0;
    cub_device_scan(NULL, workspace_size, x, y, num_items, stream,
                    op, dtype_id);
    return workspace_size;
}

/* -------- device histogram -------- */

void cub_device_histogram_range(void* workspace, size_t& workspace_size, void* x, void* y,
    int n_bins, void* bins, size_t n_samples, cudaStream_t stream, int dtype_id)
{
    // TODO(leofang): support complex
    if (dtype_id == CUPY_TYPE_COMPLEX64 || dtype_id == CUPY_TYPE_COMPLEX128) {
	    throw std::runtime_error("complex dtype is not yet supported");
    }

    // TODO(leofang): n_samples is of type size_t, but if it's < 2^31 we cast it to int later
    return dtype_dispatcher(dtype_id, _cub_histogram_range(),
                            workspace, workspace_size, x, y, n_bins, bins, n_samples, stream);
}

size_t cub_device_histogram_range_get_workspace_size(void* x, void* y, int n_bins,
    void* bins, size_t n_samples, cudaStream_t stream, int dtype_id)
{
    size_t workspace_size = 0;
    cub_device_histogram_range(NULL, workspace_size, x, y, n_bins, bins, n_samples,
                               stream, dtype_id);
    return workspace_size;
}

void cub_device_histogram_even(void* workspace, size_t& workspace_size, void* x, void* y,
    int n_bins, int lower, int upper, size_t n_samples, cudaStream_t stream, int dtype_id)
{
    #ifndef CUPY_USE_HIP
    return dtype_dispatcher(dtype_id, _cub_histogram_even(),
                            workspace, workspace_size, x, y, n_bins, lower, upper, n_samples, stream);
    #endif
}

size_t cub_device_histogram_even_get_workspace_size(void* x, void* y, int n_bins,
    int lower, int upper, size_t n_samples, cudaStream_t stream, int dtype_id)
{
    size_t workspace_size = 0;
    cub_device_histogram_even(NULL, workspace_size, x, y, n_bins, lower, upper, n_samples,
                              stream, dtype_id);
    return workspace_size;
}
