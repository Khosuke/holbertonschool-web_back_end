#!/usr/bin/env python3
"""
This module provides a type-annotated function 'sum_list'
which takes a list of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers
    Arg:
        input_list (List[float]): A list containing float values
    Returns:
        float: The total sum of all elements in the list
    """
    return sum(input_list)
