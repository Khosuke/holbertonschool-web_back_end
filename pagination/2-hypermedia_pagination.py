#!/usr/bin/env python3
"""
This module provides a `Server` class to paginate a CSV dataset
containing popular baby names.
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on the page number and page size
        Args:
            page (int): The current page number (1-indexed)
            page_size (int): The number of items per page
        Returns:
            List[List]: A list of rows corresponding to the requested page
        Raises:
            AssertionError: If page or page_size are not positive integers
        """
        assert type(page) is int and page >= 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns pagination information in a hypermedia-style format
        Args:
            page (int): The current page number (1-indexed)
            page_size (int): The number of items per page
        Returns:
            dict: A dictionary containing:
                - page_size (int): The number of items on the current page
                - page (int): The current page number.
                - data (List[List]): The actual data for the current page
                - next_page (Optional[int]): The next page number,
                    or None if no next page
                - prev_page (Optional[int]): The previous page number,
                    or None if on first page
                - total_pages (int): Total number of pages available
        """
        data = self.get_page()
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
