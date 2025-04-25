#!/usr/bin/env python3
"""
This module provides a type-annotated function 'to_kv'
that takes a string and an int OR float as arguments and returns a tuple.
The first element of the tuple is the string.
The second element is the square of the int/float annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string,
    and the second element is the square of the input number
    Args:
        k (str): A string
        v (Union[int, float]): A number (int or float) to be squared
    Returns:
        Tuple[str, float]: A tuple with a string and the square of the number
    """
    return (k, v * v)
