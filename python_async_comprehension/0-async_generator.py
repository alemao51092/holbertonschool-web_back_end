#!/usr/bin/env python3

""" shebang"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """random number between o and 10 """
    for n in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
