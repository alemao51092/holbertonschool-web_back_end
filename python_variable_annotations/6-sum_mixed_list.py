#!/usr/bin/env python3
"""shebang"""

from typing import List, Union 


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the sum of float and int  mxd_list"""
    mxdlistsum = 0
    for i in mxd_list:
        mxdlistsum = mxdlistsum + i
    return (mxdlistsum)
