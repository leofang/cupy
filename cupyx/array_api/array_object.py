"""
Function stubs for array object.

NOTE: This file is generated automatically by the generate_stubs.py script. Do
not modify it directly.

See
https://github.com/data-apis/array-api/blob/master/spec/API_specification/array_object.md
"""

from __future__ import annotations

from ._types import array
import cupy

def __abs__(x: array, /) -> array:
    """
    Note: __abs__ is a method of the array object.
    """
    return x.__abs__(x)

def __add__(x1: array, x2: array, /) -> array:
    """
    Note: __add__ is a method of the array object.
    """
    return x1.__add__(x1, x2)

def __and__(x1: array, x2: array, /) -> array:
    """
    Note: __and__ is a method of the array object.
    """
    return x1.__and__(x1, x2)

def __eq__(x1: array, x2: array, /) -> array:
    """
    Note: __eq__ is a method of the array object.
    """
    return x1.__eq__(x1, x2)

def __floordiv__(x1: array, x2: array, /) -> array:
    """
    Note: __floordiv__ is a method of the array object.
    """
    return x1.__floordiv__(x1, x2)

def __ge__(x1: array, x2: array, /) -> array:
    """
    Note: __ge__ is a method of the array object.
    """
    return x1.__ge__(x1, x2)

def __getitem__(x, key, /):
    """
    Note: __getitem__ is a method of the array object.
    """
    return x.__getitem__(x, key)

def __gt__(x1: array, x2: array, /) -> array:
    """
    Note: __gt__ is a method of the array object.
    """
    return x1.__gt__(x1, x2)

def __invert__(x: array, /) -> array:
    """
    Note: __invert__ is a method of the array object.
    """
    return x.__invert__(x)

def __le__(x1: array, x2: array, /) -> array:
    """
    Note: __le__ is a method of the array object.
    """
    return x1.__le__(x1, x2)

def __len__(x, /):
    """
    Note: __len__ is a method of the array object.
    """
    return x.__len__(x)

def __lshift__(x1: array, x2: array, /) -> array:
    """
    Note: __lshift__ is a method of the array object.
    """
    return x1.__lshift__(x1, x2)

def __lt__(x1: array, x2: array, /) -> array:
    """
    Note: __lt__ is a method of the array object.
    """
    return x1.__lt__(x1, x2)

def __matmul__(x1: array, x2: array, /) -> array:
    """
    Note: __matmul__ is a method of the array object.
    """
    return x1.__matmul__(x1, x2)

def __mod__(x1: array, x2: array, /) -> array:
    """
    Note: __mod__ is a method of the array object.
    """
    return x1.__mod__(x1, x2)

def __mul__(x1: array, x2: array, /) -> array:
    """
    Note: __mul__ is a method of the array object.
    """
    return x1.__mul__(x1, x2)

def __ne__(x1: array, x2: array, /) -> array:
    """
    Note: __ne__ is a method of the array object.
    """
    return x1.__ne__(x1, x2)

def __neg__(x: array, /) -> array:
    """
    Note: __neg__ is a method of the array object.
    """
    return x.__neg__(x)

def __or__(x1: array, x2: array, /) -> array:
    """
    Note: __or__ is a method of the array object.
    """
    return x1.__or__(x1, x2)

def __pos__(x: array, /) -> array:
    """
    Note: __pos__ is a method of the array object.
    """
    return x.__pos__(x)

def __pow__(x1: array, x2: array, /) -> array:
    """
    Note: __pow__ is a method of the array object.
    """
    return x1.__pow__(x1, x2)

def __rshift__(x1: array, x2: array, /) -> array:
    """
    Note: __rshift__ is a method of the array object.
    """
    return x1.__rshift__(x1, x2)

def __setitem__(x, key, value, /):
    """
    Note: __setitem__ is a method of the array object.
    """
    return x.__setitem__(x, key, value)

def __sub__(x1: array, x2: array, /) -> array:
    """
    Note: __sub__ is a method of the array object.
    """
    return x1.__sub__(x1, x2)

def __truediv__(x1: array, x2: array, /) -> array:
    """
    Note: __truediv__ is a method of the array object.
    """
    return x1.__truediv__(x1, x2)

def __xor__(x1: array, x2: array, /) -> array:
    """
    Note: __xor__ is a method of the array object.
    """
    return x1.__xor__(x1, x2)

# Note: dtype is an attribute of the array object.
dtype = None

# Note: device is an attribute of the array object.
device = None

# Note: ndim is an attribute of the array object.
ndim = None

# Note: shape is an attribute of the array object.
shape = None

# Note: size is an attribute of the array object.
size = None

# Note: T is an attribute of the array object.
T = None

__all__ = ['__abs__', '__add__', '__and__', '__eq__', '__floordiv__', '__ge__', '__getitem__', '__gt__', '__invert__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__or__', '__pos__', '__pow__', '__rshift__', '__setitem__', '__sub__', '__truediv__', '__xor__', 'dtype', 'device', 'ndim', 'shape', 'size', 'T']
