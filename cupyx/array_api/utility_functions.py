"""
Function stubs for utility functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/utility_functions.md
"""

from __future__ import annotations

from ._types import Optional, Tuple, Union, array
import cupy

def all(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    return cupy.all(x, axis, keepdims)

def any(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    return cupy.any(x, axis, keepdims)

__all__ = ['all', 'any']
