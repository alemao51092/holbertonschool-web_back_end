#!/usr/bin/env python3
"""
shebang

"""
from typing import List
import random
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all delay"""
    list_n = []
    for i in range(n):
        result = await wait_random(max_delay)
        list_n.append(result)
    return sorted(list_n)
