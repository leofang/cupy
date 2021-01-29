"""
Function stubs for creation functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/creation_functions.md
"""

from __future__ import annotations

from ._types import Optional, Tuple, Union, array, device, dtype

def arange(start: Union[int, float], /, *, stop: Optional[Union[int, float]] = None, step: Union[int, float] = 1, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.arange(start, stop, step, dtype, device)

def empty(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.empty(shape, dtype, device)

def empty_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.empty_like(x, dtype, device)

def eye(N: int, /, *, M: Optional[int] = None, k: Optional[int] = 0, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.eye(N, M, k, dtype, device)

def full(shape: Union[int, Tuple[int, ...]], fill_value: Union[int, float], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.full(shape, fill_value, dtype, device)

def full_like(x: array, fill_value: Union[int, float], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.full_like(x, fill_value, dtype, device)

def linspace(start: Union[int, float], stop: Union[int, float], num: int, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None, endpoint: bool = True) -> array:
    #pass
    cupy.linspace(start, stop, num, dtype, device, endpoint)

def ones(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.ones(shape, dtype, device)

def ones_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.ones_like(x, dtype, device)

def zeros(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.zeros(shape, dtype, device)

def zeros_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    #pass
    cupy.zeros_like(x, dtype, device)

__all__ = ['arange', 'empty', 'empty_like', 'eye', 'full', 'full_like', 'linspace', 'ones', 'ones_like', 'zeros', 'zeros_like']
