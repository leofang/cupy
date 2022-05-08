import cupy
from cupy.cuda import cub


def segmented_sort(keys, offsets, values=None, ascending=True):
    # TODO(leofang): add docstring
    # TODO(leofang): add sanity checks
    return cub.device_segmented_sort(keys, offsets, values, ascending)
