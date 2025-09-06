#!/usr/bin/env python3
"""multiple coroutines with async"""
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
            for d in delays:
                if rd < d or rd == d:
                    delays.insert(delays.index(d), rd)
                    break
                elif rd > delays[len(delays) - 1]:
                    delays.append(rd)
                    break
    return delays
