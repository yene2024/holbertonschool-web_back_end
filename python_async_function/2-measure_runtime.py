#!/usr/bin/env python3
""" Measuring runtime """
from asyncio import run
from time import perf_counter

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns the time """
    start = perf_counter()
    run(wait_n(n, max_delay))
    stop = perf_counter()
    return (stop - start)/n
