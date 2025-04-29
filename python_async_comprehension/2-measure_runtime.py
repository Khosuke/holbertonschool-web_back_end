#!/usr/bin/env python3
"""
This module measures the total runtime of executing multiple
asynchronous comprehensions concurrently.
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running four 'async_comprehension'
    coroutines concurrently
    Returns:
        float: The total elapsed time in seconds
    """
    start = time()
    await gather(*(async_comprehension() for i in range(4)))
    end = time()
    return end - start
