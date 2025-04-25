#!/usr/bin/env python3
"""
This module provides a function 'element_lenght'
that compute the length of each element in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each containing an element and its length
    Arg:
        lst (Iterable[Sequence]): An iterable of sequences
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
            where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
