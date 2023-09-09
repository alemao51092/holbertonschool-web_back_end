#!/usr/bin/env python3
"""Task 0:
    Simple helper function"""
import csv
import math
from typing import List, Dict
import math


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
        "get_page() method of Server class"
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        first = indexes[0]
        last = indexes[1]

        return self.dataset()[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        "get_hyper() method for Server class"
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }


def index_range(page, page_size) -> tuple:
    """index_range() function"""
    return (page * page_size) - page_size, page * page_size
