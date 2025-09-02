#!/usr/bin/env python3
"""duck type an iterable object"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple]:
    """return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
