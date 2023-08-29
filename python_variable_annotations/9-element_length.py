#!/usr/bin/env python3
"""shebang"""

from typing import List, Tuple, Iterable, Sequence, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:  # Noqa: E501
    """element"""
    return [(i, len(i)) for i in lst]
