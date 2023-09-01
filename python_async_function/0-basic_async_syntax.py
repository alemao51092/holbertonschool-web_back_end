#!/usr/bin/env python3
"""
Async Wait Random Function

"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously waits for a random delay."""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
