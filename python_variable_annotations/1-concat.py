#!/usr/bin/env python3
"""
This module provides a type-annotated function 'concat'
that takes two strings as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings
    Args:
        str1 (str): The first string
        str2 (str): The second string
    Returns:
        str: A New string of str1 followed by str2
    """
    return str1 + str2
