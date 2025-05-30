#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        Return paginated data with resilience to deletions in the dataset
        Args:
            index (int): The current start index (must be within valid range)
            page_size (int): The number of items to return
        Returns:
            Dict[str, Any]: A dictionary with pagination metadata:
                - index: the original index queried
                - next_index: the index to use for the next query
                - page_size: the number of items returned
                - data: the list of items on the current page
        """
        assert type(index) is int and 0 <= index < len(self.dataset())

        index = 0 if index is None else index
        dataset = self.indexed_dataset()

        assert index < len(dataset)

        data = []
        nb_elements = 0
        new_index = index

        while new_index < len(dataset) and nb_elements < page_size:
            if new_index in dataset:
                data.append(dataset[new_index])
                nb_elements += 1
            new_index += 1

        return {
            "index": index,
            "next_index": new_index,
            "page_size": page_size,
            "data": data
        }
