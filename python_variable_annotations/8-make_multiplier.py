#!/usr/bin/env python3
"""shebang"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier funcation"""
    def multiplier_float(z: float) -> float:
        """function float * float"""
        return (z * multiplier)
    return multiplier_float
