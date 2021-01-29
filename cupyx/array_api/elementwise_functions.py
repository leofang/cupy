"""
Function stubs for elementwise functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/elementwise_functions.md
"""

from __future__ import annotations

from ._types import array
import cupy

def abs(x: array, /) -> array:
    return cupy.abs(x)

def acos(x: array, /) -> array:
    return cupy.acos(x)

def acosh(x: array, /) -> array:
    return cupy.acosh(x)

def add(x1: array, x2: array, /) -> array:
    return cupy.add(x1, x2)

def asin(x: array, /) -> array:
    return cupy.asin(x)

def asinh(x: array, /) -> array:
    return cupy.asinh(x)

def atan(x: array, /) -> array:
    return cupy.atan(x)

def atan2(x1: array, x2: array, /) -> array:
    return cupy.atan2(x1, x2)

def atanh(x: array, /) -> array:
    return cupy.atanh(x)

def bitwise_and(x1: array, x2: array, /) -> array:
    return cupy.bitwise_and(x1, x2)

def bitwise_left_shift(x1: array, x2: array, /) -> array:
    return cupy.bitwise_left_shift(x1, x2)

def bitwise_invert(x: array, /) -> array:
    return cupy.bitwise_invert(x)

def bitwise_or(x1: array, x2: array, /) -> array:
    return cupy.bitwise_or(x1, x2)

def bitwise_right_shift(x1: array, x2: array, /) -> array:
    return cupy.bitwise_right_shift(x1, x2)

def bitwise_xor(x1: array, x2: array, /) -> array:
    return cupy.bitwise_xor(x1, x2)

def ceil(x: array, /) -> array:
    return cupy.ceil(x)

def cos(x: array, /) -> array:
    return cupy.cos(x)

def cosh(x: array, /) -> array:
    return cupy.cosh(x)

def divide(x1: array, x2: array, /) -> array:
    return cupy.divide(x1, x2)

def equal(x1: array, x2: array, /) -> array:
    return cupy.equal(x1, x2)

def exp(x: array, /) -> array:
    return cupy.exp(x)

def expm1(x: array, /) -> array:
    return cupy.expm1(x)

def floor(x: array, /) -> array:
    return cupy.floor(x)

def floor_divide(x1: array, x2: array, /) -> array:
    return cupy.floor_divide(x1, x2)

def greater(x1: array, x2: array, /) -> array:
    return cupy.greater(x1, x2)

def greater_equal(x1: array, x2: array, /) -> array:
    return cupy.greater_equal(x1, x2)

def isfinite(x: array, /) -> array:
    return cupy.isfinite(x)

def isinf(x: array, /) -> array:
    return cupy.isinf(x)

def isnan(x: array, /) -> array:
    return cupy.isnan(x)

def less(x1: array, x2: array, /) -> array:
    return cupy.less(x1, x2)

def less_equal(x1: array, x2: array, /) -> array:
    return cupy.less_equal(x1, x2)

def log(x: array, /) -> array:
    return cupy.log(x)

def log1p(x: array, /) -> array:
    return cupy.log1p(x)

def log2(x: array, /) -> array:
    return cupy.log2(x)

def log10(x: array, /) -> array:
    return cupy.log10(x)

def logical_and(x1: array, x2: array, /) -> array:
    return cupy.logical_and(x1, x2)

def logical_not(x: array, /) -> array:
    return cupy.logical_not(x)

def logical_or(x1: array, x2: array, /) -> array:
    return cupy.logical_or(x1, x2)

def logical_xor(x1: array, x2: array, /) -> array:
    return cupy.logical_xor(x1, x2)

def multiply(x1: array, x2: array, /) -> array:
    return cupy.multiply(x1, x2)

def negative(x: array, /) -> array:
    return cupy.negative(x)

def not_equal(x1: array, x2: array, /) -> array:
    return cupy.not_equal(x1, x2)

def positive(x: array, /) -> array:
    return cupy.positive(x)

def pow(x1: array, x2: array, /) -> array:
    return cupy.pow(x1, x2)

def remainder(x1: array, x2: array, /) -> array:
    return cupy.remainder(x1, x2)

def round(x: array, /) -> array:
    return cupy.round(x)

def sign(x: array, /) -> array:
    return cupy.sign(x)

def sin(x: array, /) -> array:
    return cupy.sin(x)

def sinh(x: array, /) -> array:
    return cupy.sinh(x)

def square(x: array, /) -> array:
    return cupy.square(x)

def sqrt(x: array, /) -> array:
    return cupy.sqrt(x)

def subtract(x1: array, x2: array, /) -> array:
    return cupy.subtract(x1, x2)

def tan(x: array, /) -> array:
    return cupy.tan(x)

def tanh(x: array, /) -> array:
    return cupy.tanh(x)

def trunc(x: array, /) -> array:
    return cupy.trunc(x)

__all__ = ['abs', 'acos', 'acosh', 'add', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'bitwise_and', 'bitwise_left_shift', 'bitwise_invert', 'bitwise_or', 'bitwise_right_shift', 'bitwise_xor', 'ceil', 'cos', 'cosh', 'divide', 'equal', 'exp', 'expm1', 'floor', 'floor_divide', 'greater', 'greater_equal', 'isfinite', 'isinf', 'isnan', 'less', 'less_equal', 'log', 'log1p', 'log2', 'log10', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'multiply', 'negative', 'not_equal', 'positive', 'pow', 'remainder', 'round', 'sign', 'sin', 'sinh', 'square', 'sqrt', 'subtract', 'tan', 'tanh', 'trunc']
