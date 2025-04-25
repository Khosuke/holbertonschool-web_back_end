#!/usr/bin/env python3
"""
This module provides a type-annotated function 'floor'
which takes a float 'n' as argument and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of the float
    Arg:
        n (float): The number to floor
    Returns:
        int: The floor of the number as an integer
    """
    return math.floor(n)
