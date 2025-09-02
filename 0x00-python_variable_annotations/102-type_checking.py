#!/usr/bin/env python3
"""type checking with My[Py]"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
