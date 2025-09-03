#!/usr/bin/env python3
"""multiple coroutines with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all thewait_random(max_delay)"""
    delays = []
    for x in range(n):
        rd = await wait_random(max_delay)
        delays.append(rd)
    return delays
