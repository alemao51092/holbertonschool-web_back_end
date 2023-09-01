#!/usr/bin/env python3
"""shebang"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """botellas caras"""
    async_list = [i async for i in async_generator()]
    return async_list
