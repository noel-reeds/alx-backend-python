#!/usr/bin/env python3
"""multiple coroutines with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all wait_random(max_delay)"""
    delays: List[float] = []
    for m in range(n):
        rd = await wait_random(max_delay)
        if len(delays) < 1:
            delays.append(rd)
        else:
            for i in range(len(delays)):
                if rd < delays[i] or rd == delays[i]:
                    delays.insert(i, rd)
                    break
                else:
                    i += 1
    return delays
