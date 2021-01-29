"""
Function stubs for statistical functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/statistical_functions.md
"""

from __future__ import annotations

from ._types import Optional, Tuple, Union, array

def max(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    #pass
    cupy.max(x, axis, keepdims)

def mean(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    #pass
    cupy.mean(x, axis, keepdims)

def min(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    #pass
    cupy.min(x, axis, keepdims)

def prod(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    #pass
    cupy.prod(x, axis, keepdims)

def std(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, correction: Union[int, float] = 0.0, keepdims: bool = False) -> array:
    #pass
    cupy.std(x, axis, correction, keepdims)

def sum(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, keepdims: bool = False) -> array:
    #pass
    cupy.sum(x, axis, keepdims)

def var(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None, correction: Union[int, float] = 0.0, keepdims: bool = False) -> array:
    #pass
    cupy.var(x, axis, correction, keepdims)

__all__ = ['max', 'mean', 'min', 'prod', 'std', 'sum', 'var']
