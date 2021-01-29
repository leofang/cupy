"""
Function stubs for sorting functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/sorting_functions.md
"""

from __future__ import annotations

from ._types import array

def argsort(x: array, /, *, axis: int = -1, descending: bool = False, stable: bool = True) -> array:
    #pass
    cupy.argsort(x, axis, descending, stable)

def sort(x: array, /, *, axis: int = -1, descending: bool = False, stable: bool = True) -> array:
    #pass
    cupy.sort(x, axis, descending, stable)

__all__ = ['argsort', 'sort']
