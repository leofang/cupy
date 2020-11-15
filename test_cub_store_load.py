import cupy as cp
import numpy as np
from cupyx.time import repeat


code = r'''
#include <cupy/cub/cub/block/block_load.cuh>
#include <cupy/cub/cub/block/block_store.cuh>

// Compile-time constants for CUB template specializations
#define ITEMS_PER_THREAD  4
#define BLOCK_SIZE        256

#define TYPE_IN  double
#define TYPE_OUT double


extern "C"
__global__ void my_sin(void* in_arr, void* out_arr, size_t _array_size, size_t _segment_size) {
  unsigned int tid = threadIdx.x;

  // Specialize BlockLoad type for faster (?) loading
  typedef cub::BlockLoad<TYPE_IN, BLOCK_SIZE, ITEMS_PER_THREAD,
                         cub::BLOCK_LOAD_DIRECT> BlockLoadT;

  // Shared memory for loading
  __shared__ typename BlockLoadT::TempStorage temp_storage_load;

  // Specialize BlockStore type for faster (?) storing
  typedef cub::BlockStore<TYPE_OUT, BLOCK_SIZE, ITEMS_PER_THREAD,
                          cub::BLOCK_STORE_DIRECT> BlockStoreT;

  // Shared memory for storing
  __shared__ typename BlockStoreT::TempStorage temp_storage_store;

  // input & output raw pointers
  const TYPE_IN* _in0 = (const TYPE_IN*)in_arr;
  TYPE_OUT* _out0 = (TYPE_OUT*)out_arr;

  // Per-thread tile data
  TYPE_IN _sdata[ITEMS_PER_THREAD];
  #pragma unroll
  for (int j = 0; j < ITEMS_PER_THREAD; j++) {
      _sdata[j] = TYPE_IN(0);
  }

  // each block handles 1 segment
  size_t segment_idx = blockIdx.x * _segment_size;
  const TYPE_IN* in_seg_head = _in0 + segment_idx;
  TYPE_OUT* out_seg_head = _out0 + segment_idx;
  size_t i = 0;  // tile head within the segment
  int tile_size = BLOCK_SIZE * ITEMS_PER_THREAD;

  // "last segment" is special: it might be shorter
  if (_array_size - segment_idx <= _segment_size) {
      _segment_size = _array_size - segment_idx;
  }

  // loop over tiles within 1 segment
  for (i=0; i<_segment_size; i+=BLOCK_SIZE*ITEMS_PER_THREAD) {
    // for the last tile
    if (_segment_size - i <= tile_size) { tile_size = _segment_size - i; }

    // load a tile
    BlockLoadT(temp_storage_load).Load(in_seg_head + i, _sdata, tile_size);

    // computation
    #pragma unroll
    for (int j = 0; j < ITEMS_PER_THREAD; j++) {
        _sdata[j] = sin(_sdata[j]);
    }

    // store a tile
    BlockStoreT(temp_storage_store).Store(out_seg_head + i, _sdata, tile_size);

    //__syncthreads();  // for reusing temp_storage
  }
}
'''

ker = cp.RawKernel(code, 'my_sin', options=('-std=c++11',), jitify=True)

#a = cp.random.random(10000000)
a = cp.random.random(200000000)
b = cp.empty_like(a)
#print(a.dtype)

items_per_thread = 4
block_size = 256
#segment_size = 2048
segment_size = 1*block_size * items_per_thread
contiguous_size = a.size
num_segments = (contiguous_size + segment_size - 1) // segment_size

args = ((num_segments,), (block_size,), (a, b, contiguous_size, segment_size))
print(repeat(ker, args, n_repeat=100))
print(repeat(cp.sin, (a,), n_repeat=100))

a_np = cp.asnumpy(a)
b_np = np.sin(a_np)
#print(cp.where(cp.abs(cp.asarray(b_np) - b) > 1E-4))
print(cp.allclose(b_np, b))
