#!/usr/bin/env python3
"""
This module providesa type-annotated function 'make_multiplier'
that takes a float as argument and returns a function
that multiplies another float by the first float.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function
    Arg:
        multiplier (float): The number to multiply by
    Returns:
        Callable[[float], float]: A function that takes a float and
            returns the result of multiplying it by 'multiplier'
    """
    def apply_multiplier(num: float) -> float:
        return num * multiplier
    return apply_multiplier
