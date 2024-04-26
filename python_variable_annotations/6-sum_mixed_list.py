#!/usr/bin/env python3
"""Writing a type-annotated function sum_mixed_list
which takes a list mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of integers and floats in the mixed list."""
    return sum(mxd_lst)
