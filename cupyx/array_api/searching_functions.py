"""
Function stubs for searching functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/searching_functions.md
"""

from __future__ import annotations

from ._types import Tuple, array
import cupy

def argmax(x: array, /, *, axis: int = None, keepdims: bool = False) -> array:
    return cupy.argmax(x, axis, keepdims)

def argmin(x: array, /, *, axis: int = None, keepdims: bool = False) -> array:
    return cupy.argmin(x, axis, keepdims)

def nonzero(x: array, /) -> Tuple[array, ...]:
    return cupy.nonzero(x)

def where(condition: array, x1: array, x2: array, /) -> array:
    return cupy.where(condition, x1, x2)

__all__ = ['argmax', 'argmin', 'nonzero', 'where']
