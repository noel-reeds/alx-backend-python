#!/usr/bin/env python3
"""complex types - functions"""
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def returned_func(value: float) -> float:
        """returns arg * multiplier"""
        return value * multiplier
    return returned_func
