#!/usr/bin/env python3
"""complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of string and square"""
    return (k, v * v)
