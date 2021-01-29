"""
Function stubs for creation functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/creation_functions.md
"""

from __future__ import annotations

from ._types import Optional, Tuple, Union, array, device, dtype
import cupy

def arange(start: Union[int, float], /, *, stop: Optional[Union[int, float]] = None, step: Union[int, float] = 1, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.arange(start, stop, step, dtype)
    else:
        with device:
            return cupy.arange(start, stop, step, dtype)

def empty(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.empty(shape, dtype)
    else:
        with device:
            return cupy.empty(shape, dtype)

def empty_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.empty_like(x, dtype)
    else:
        with device:
            return cupy.empty_like(x, dtype)

def eye(N: int, /, *, M: Optional[int] = None, k: Optional[int] = 0, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.eye(N, M, k, dtype)
    else:
        with device:
            return cupy.eye(N, M, k, dtype)

def full(shape: Union[int, Tuple[int, ...]], fill_value: Union[int, float], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.full(shape, fill_value, dtype)
    else:
        with device:
            return cupy.full(shape, fill_value, dtype)

def full_like(x: array, fill_value: Union[int, float], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.full_like(x, fill_value, dtype)
    else:
        with device:
            return cupy.full_like(x, fill_value, dtype)

def linspace(start: Union[int, float], stop: Union[int, float], num: int, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None, endpoint: bool = True) -> array:
    if device is None:
        return cupy.linspace(start, stop, num, dtype, endpoint)
    else:
        with device:
            return cupy.linspace(start, stop, num, dtype, endpoint)

def ones(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.ones(shape, dtype)
    else:
        with device:
            return cupy.ones(shape, dtype)

def ones_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.ones_like(x, dtype)
    else:
        with device:
            return cupy.ones_like(x, dtype)

def zeros(shape: Union[int, Tuple[int, ...]], /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.zeros(shape, dtype)
    else:
        with device:
            return cupy.zeros(shape, dtype)

def zeros_like(x: array, /, *, dtype: Optional[dtype] = None, device: Optional[device] = None) -> array:
    if device is None:
        return cupy.zeros_like(x, dtype)
    else:
        with device:
            return cupy.zeros_like(x, dtype)

__all__ = ['arange', 'empty', 'empty_like', 'eye', 'full', 'full_like', 'linspace', 'ones', 'ones_like', 'zeros', 'zeros_like']
