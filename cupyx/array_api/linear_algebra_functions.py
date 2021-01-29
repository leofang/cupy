"""
Function stubs for linear algebra functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/linear_algebra_functions.md
"""

from __future__ import annotations

from ._types import Literal, Optional, Tuple, Union, array
from .constants import inf
import cupy

def cholesky():
    return cupy.cholesky()

def cross(x1: array, x2: array, /, *, axis: int = -1) -> array:
    return cupy.cross(x1, x2, axis)

def det(x: array, /) -> array:
    return cupy.det(x)

def diagonal(x: array, /, *, axis1: int = 0, axis2: int = 1, offset: int = 0) -> array:
    return cupy.diagonal(x, axis1, axis2, offset)

def dot():
    return cupy.dot()

def eig():
    return cupy.eig()

def eigvalsh():
    return cupy.eigvalsh()

def einsum():
    return cupy.einsum()

def inv(x: array, /) -> array:
    return cupy.inv(x)

def lstsq():
    return cupy.lstsq()

def matmul():
    return cupy.matmul()

def matrix_power():
    return cupy.matrix_power()

def matrix_rank():
    return cupy.matrix_rank()

def norm(x: array, /, *, axis: Optional[Union[int, Tuple[int, int]]] = None, keepdims: bool = False, ord: Optional[Union[int, float, Literal[inf, -inf, 'fro', 'nuc']]] = None) -> array:
    return cupy.norm(x, axis, keepdims, ord)

def outer(x1: array, x2: array, /) -> array:
    return cupy.outer(x1, x2)

def pinv():
    return cupy.pinv()

def qr():
    return cupy.qr()

def slogdet():
    return cupy.slogdet()

def solve():
    return cupy.solve()

def svd():
    return cupy.svd()

def trace(x: array, /, *, axis1: int = 0, axis2: int = 1, offset: int = 0) -> array:
    return cupy.trace(x, axis1, axis2, offset)

def transpose(x: array, /, *, axes: Optional[Tuple[int, ...]] = None) -> array:
    return cupy.transpose(x, axes)

__all__ = ['cholesky', 'cross', 'det', 'diagonal', 'dot', 'eig', 'eigvalsh', 'einsum', 'inv', 'lstsq', 'matmul', 'matrix_power', 'matrix_rank', 'norm', 'outer', 'pinv', 'qr', 'slogdet', 'solve', 'svd', 'trace', 'transpose']
