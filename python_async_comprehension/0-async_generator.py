#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random float numbers
between 0 and 10, simulating delays between each generation.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, ]:
    """
    Asynchronously yield 10 random float numbers between 0 and 10
    Each number is generated after a 1-second asynchronous delay
    Yields:
        float: A random float between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
