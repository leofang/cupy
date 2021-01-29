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

def cholesky():
    #pass
    cupy.cholesky()

def cross(x1: array, x2: array, /, *, axis: int = -1) -> array:
    #pass
    cupy.cross(x1, x2, axis)

def det(x: array, /) -> array:
    #pass
    cupy.det(x)

def diagonal(x: array, /, *, axis1: int = 0, axis2: int = 1, offset: int = 0) -> array:
    #pass
    cupy.diagonal(x, axis1, axis2, offset)

def dot():
    #pass
    cupy.dot()

def eig():
    #pass
    cupy.eig()

def eigvalsh():
    #pass
    cupy.eigvalsh()

def einsum():
    #pass
    cupy.einsum()

def inv(x: array, /) -> array:
    #pass
    cupy.inv(x)

def lstsq():
    #pass
    cupy.lstsq()

def matmul():
    #pass
    cupy.matmul()

def matrix_power():
    #pass
    cupy.matrix_power()

def matrix_rank():
    #pass
    cupy.matrix_rank()

def norm(x: array, /, *, axis: Optional[Union[int, Tuple[int, int]]] = None, keepdims: bool = False, ord: Optional[Union[int, float, Literal[inf, -inf, 'fro', 'nuc']]] = None) -> array:
    #pass
    cupy.norm(x, axis, keepdims, ord)

def outer(x1: array, x2: array, /) -> array:
    #pass
    cupy.outer(x1, x2)

def pinv():
    #pass
    cupy.pinv()

def qr():
    #pass
    cupy.qr()

def slogdet():
    #pass
    cupy.slogdet()

def solve():
    #pass
    cupy.solve()

def svd():
    #pass
    cupy.svd()

def trace(x: array, /, *, axis1: int = 0, axis2: int = 1, offset: int = 0) -> array:
    #pass
    cupy.trace(x, axis1, axis2, offset)

def transpose(x: array, /, *, axes: Optional[Tuple[int, ...]] = None) -> array:
    #pass
    cupy.transpose(x, axes)

__all__ = ['cholesky', 'cross', 'det', 'diagonal', 'dot', 'eig', 'eigvalsh', 'einsum', 'inv', 'lstsq', 'matmul', 'matrix_power', 'matrix_rank', 'norm', 'outer', 'pinv', 'qr', 'slogdet', 'solve', 'svd', 'trace', 'transpose']
