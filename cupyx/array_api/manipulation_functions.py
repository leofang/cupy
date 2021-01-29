"""
Function stubs for manipulation functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/manipulation_functions.md
"""

from __future__ import annotations

from ._types import Optional, Tuple, Union, array

def concat(arrays: Tuple[array], /, *, axis: Optional[int] = 0) -> array:
    #pass
    cupy.concat(arrays, axis)

def expand_dims(x: array, axis: int, /) -> array:
    #pass
    cupy.expand_dims(x, axis)

def flip(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> array:
    #pass
    cupy.flip(x, axis)

def reshape(x: array, shape: Tuple[int, ...], /) -> array:
    #pass
    cupy.reshape(x, shape)

def roll(x: array, shift: Union[int, Tuple[int, ...]], /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> array:
    #pass
    cupy.roll(x, shift, axis)

def squeeze(x: array, /, *, axis: Optional[Union[int, Tuple[int, ...]]] = None) -> array:
    #pass
    cupy.squeeze(x, axis)

def stack(arrays: Tuple[array], /, *, axis: int = 0) -> array:
    #pass
    cupy.stack(arrays, axis)

__all__ = ['concat', 'expand_dims', 'flip', 'reshape', 'roll', 'squeeze', 'stack']
