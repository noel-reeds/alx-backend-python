#!/usr/bin/env python3
"""multiple coroutines with async"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all wait_random(max_delay)"""
    tasks: List[float] = []
    for m in range(n):
        rd = await task_wait_random(max_delay)
        if len(tasks) < 1:
            tasks.append(rd)
        else:
            for d in tasks:
                if rd < d or rd == d:
                    tasks.insert(tasks.index(d), rd)
                    break
                elif rd > tasks[len(tasks) - 1]:
                    tasks.append(rd)
                    break
    return tasks
