"""
cuDNN Wrapper

Use `cupy_backends.libs.cudnn` directly in CuPy codebase.
"""

available = True

try:
    from cupy_backends.libs.cudnn import *  # NOQA
except ImportError as e:
    available = False
    from cupy._environment import _preload_warning
    _preload_warning('cudnn', e)
