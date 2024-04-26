#!/usr/bin/env python3
"""
Function make_multiplier takes float multiplier as argument
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return mult function"""

    def mult(n: float) -> float:
        return n * multiplier

    return mult
