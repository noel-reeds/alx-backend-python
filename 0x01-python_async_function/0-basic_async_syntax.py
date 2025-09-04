#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay and returns it"""
    await asyncio.sleep(rd := random.uniform(0, max_delay))
    return rd
