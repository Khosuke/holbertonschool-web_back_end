#!/usr/bin/env python3
"""
This module provides a type-annotated function 'sum_mixed_list'
which takes a list of integers and floats and returns their sum as a float.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats
    Args:
        mxd_lst (List[Union[int, float]]): A list of ints and floats numbers
    Returns:
        float: The total sum of all elements in the list as a float
    """
    return sum(mxd_lst)
