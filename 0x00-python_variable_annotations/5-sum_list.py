#!/usr/bin/env python3
"""complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns their sum as a float"""
    return sum(i for i in input_list)
