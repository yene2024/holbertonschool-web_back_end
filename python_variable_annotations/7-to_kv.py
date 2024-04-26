#!/usr/bin/env python3
"""Writing a type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is the string k
    and the second element is the square of the int/float v."""
    return (k, v ** 2)
