#!/usr/bin/env python3
"""asyncio tasks"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of asyncio tasks"""
    tasks = []
    for x in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    return tasks
