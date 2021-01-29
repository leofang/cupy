"""
Function stubs for elementwise functions.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/elementwise_functions.md
"""

from __future__ import annotations

from ._types import array

def abs(x: array, /) -> array:
    #pass
    cupy.abs(x)

def acos(x: array, /) -> array:
    #pass
    cupy.acos(x)

def acosh(x: array, /) -> array:
    #pass
    cupy.acosh(x)

def add(x1: array, x2: array, /) -> array:
    #pass
    cupy.add(x1, x2)

def asin(x: array, /) -> array:
    #pass
    cupy.asin(x)

def asinh(x: array, /) -> array:
    #pass
    cupy.asinh(x)

def atan(x: array, /) -> array:
    #pass
    cupy.atan(x)

def atan2(x1: array, x2: array, /) -> array:
    #pass
    cupy.atan2(x1, x2)

def atanh(x: array, /) -> array:
    #pass
    cupy.atanh(x)

def bitwise_and(x1: array, x2: array, /) -> array:
    #pass
    cupy.bitwise_and(x1, x2)

def bitwise_left_shift(x1: array, x2: array, /) -> array:
    #pass
    cupy.bitwise_left_shift(x1, x2)

def bitwise_invert(x: array, /) -> array:
    #pass
    cupy.bitwise_invert(x)

def bitwise_or(x1: array, x2: array, /) -> array:
    #pass
    cupy.bitwise_or(x1, x2)

def bitwise_right_shift(x1: array, x2: array, /) -> array:
    #pass
    cupy.bitwise_right_shift(x1, x2)

def bitwise_xor(x1: array, x2: array, /) -> array:
    #pass
    cupy.bitwise_xor(x1, x2)

def ceil(x: array, /) -> array:
    #pass
    cupy.ceil(x)

def cos(x: array, /) -> array:
    #pass
    cupy.cos(x)

def cosh(x: array, /) -> array:
    #pass
    cupy.cosh(x)

def divide(x1: array, x2: array, /) -> array:
    #pass
    cupy.divide(x1, x2)

def equal(x1: array, x2: array, /) -> array:
    #pass
    cupy.equal(x1, x2)

def exp(x: array, /) -> array:
    #pass
    cupy.exp(x)

def expm1(x: array, /) -> array:
    #pass
    cupy.expm1(x)

def floor(x: array, /) -> array:
    #pass
    cupy.floor(x)

def floor_divide(x1: array, x2: array, /) -> array:
    #pass
    cupy.floor_divide(x1, x2)

def greater(x1: array, x2: array, /) -> array:
    #pass
    cupy.greater(x1, x2)

def greater_equal(x1: array, x2: array, /) -> array:
    #pass
    cupy.greater_equal(x1, x2)

def isfinite(x: array, /) -> array:
    #pass
    cupy.isfinite(x)

def isinf(x: array, /) -> array:
    #pass
    cupy.isinf(x)

def isnan(x: array, /) -> array:
    #pass
    cupy.isnan(x)

def less(x1: array, x2: array, /) -> array:
    #pass
    cupy.less(x1, x2)

def less_equal(x1: array, x2: array, /) -> array:
    #pass
    cupy.less_equal(x1, x2)

def log(x: array, /) -> array:
    #pass
    cupy.log(x)

def log1p(x: array, /) -> array:
    #pass
    cupy.log1p(x)

def log2(x: array, /) -> array:
    #pass
    cupy.log2(x)

def log10(x: array, /) -> array:
    #pass
    cupy.log10(x)

def logical_and(x1: array, x2: array, /) -> array:
    #pass
    cupy.logical_and(x1, x2)

def logical_not(x: array, /) -> array:
    #pass
    cupy.logical_not(x)

def logical_or(x1: array, x2: array, /) -> array:
    #pass
    cupy.logical_or(x1, x2)

def logical_xor(x1: array, x2: array, /) -> array:
    #pass
    cupy.logical_xor(x1, x2)

def multiply(x1: array, x2: array, /) -> array:
    #pass
    cupy.multiply(x1, x2)

def negative(x: array, /) -> array:
    #pass
    cupy.negative(x)

def not_equal(x1: array, x2: array, /) -> array:
    #pass
    cupy.not_equal(x1, x2)

def positive(x: array, /) -> array:
    #pass
    cupy.positive(x)

def pow(x1: array, x2: array, /) -> array:
    #pass
    cupy.pow(x1, x2)

def remainder(x1: array, x2: array, /) -> array:
    #pass
    cupy.remainder(x1, x2)

def round(x: array, /) -> array:
    #pass
    cupy.round(x)

def sign(x: array, /) -> array:
    #pass
    cupy.sign(x)

def sin(x: array, /) -> array:
    #pass
    cupy.sin(x)

def sinh(x: array, /) -> array:
    #pass
    cupy.sinh(x)

def square(x: array, /) -> array:
    #pass
    cupy.square(x)

def sqrt(x: array, /) -> array:
    #pass
    cupy.sqrt(x)

def subtract(x1: array, x2: array, /) -> array:
    #pass
    cupy.subtract(x1, x2)

def tan(x: array, /) -> array:
    #pass
    cupy.tan(x)

def tanh(x: array, /) -> array:
    #pass
    cupy.tanh(x)

def trunc(x: array, /) -> array:
    #pass
    cupy.trunc(x)

__all__ = ['abs', 'acos', 'acosh', 'add', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'bitwise_and', 'bitwise_left_shift', 'bitwise_invert', 'bitwise_or', 'bitwise_right_shift', 'bitwise_xor', 'ceil', 'cos', 'cosh', 'divide', 'equal', 'exp', 'expm1', 'floor', 'floor_divide', 'greater', 'greater_equal', 'isfinite', 'isinf', 'isnan', 'less', 'less_equal', 'log', 'log1p', 'log2', 'log10', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'multiply', 'negative', 'not_equal', 'positive', 'pow', 'remainder', 'round', 'sign', 'sin', 'sinh', 'square', 'sqrt', 'subtract', 'tan', 'tanh', 'trunc']
