#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """yield random numbers"""
    for i in range(10):
        rd = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rd
