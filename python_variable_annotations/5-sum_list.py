#!/usr/bin/env python3
"""shebang"""


from typing import List


def sum_list(imput_list: List[float]) -> float:
    """return the sum of float"""
    sumfloat = 0
    for i in imput_list:
        sumfloat = sumfloat + i
    return sumfloat
