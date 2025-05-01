#!/usr/bin/env python3
"""
This module provides a helper function for pagination index calculation.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination
        based on the page number and page size
    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page
    Returns:
        tuple: A tuple of two integers (start_index, end_index) representing
            the range of items to return for the given page
    """
    return (((page - 1) * page_size), page_size * page)
