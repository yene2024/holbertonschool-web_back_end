#!/usr/bin/env python3
"""Creating a measure_time function with integers
"""
import time
from typing import List
from concurrent.futures import ProcessPoolExecutor
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each wait_n call.

    Returns:
        float: Average execution time per call to wait_n.
    """
    start_time = time.time()  # Record the start time

    # Measure the total execution time of wait_n(n, max_delay)
    total_time = run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time

    # Calculate the average execution time per call
    avg_time_per_call = (end_time - start_time) / n

    return avg_time_per_call


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
