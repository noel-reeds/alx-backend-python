#!/usr/bin/env python3
"""Run-time for four parallel comprehensions"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times concurrently"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension(r) for r in range(5)))
    end = time.perf_counter()
    return end - start
