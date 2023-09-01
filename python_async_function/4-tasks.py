#!/usr/bin/env python3
"""
shebang

"""
from typing import List
import random
import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all delay"""
    list_n = []
    for i in range(n):
        result = await task_wait_random(max_delay)
        list_n.append(result)
    return sorted(list_n)
