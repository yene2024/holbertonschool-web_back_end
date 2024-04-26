#!/usr/bin/env python3
import asyncio
from typing import List
from itertools import repeat
from concurrent.futures import ProcessPoolExecutor

wait_random = __import__('0-basic_async_syntax').wait_random  # Importing wait_random from the previous file


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = []
    with ProcessPoolExecutor() as executor:
        # Create a list of tasks for wait_random
        tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
        
        # Await all tasks concurrently
        for task in asyncio.as_completed(tasks):
            delay = await task
            delays.append(delay)
    return delays


async def main():
    """Principal function."""
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))


if __name__ == "__main__":
    asyncio.run(main())
