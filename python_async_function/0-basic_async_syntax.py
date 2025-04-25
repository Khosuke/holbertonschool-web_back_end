#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine named 'wait_random'
that waits for a random delay and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time, then return the delay
    Arg:
        max_delay (int): The maximum delay in seconds (default is 10)
    Returns:
        float: The actual delay time in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
