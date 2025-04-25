#!/usr/bin/env python3
"""
This module imports an asynchronous function to simulate a random delay and
provides a function that runs multiple instances of the delay concurrently
and returns the results in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn n instances of wait_random concurrently
        and return a list of the delays
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call
    Returns:
        List[float]: A list of float delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
