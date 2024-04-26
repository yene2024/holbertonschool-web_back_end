#!/usr/bin/env python3
"""Writing an asynchronous coroutine that 
akes in an integer argument 
"""


import asyncio
import random

async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive).
    
    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay that was waited for.
    """
    # Generate a random delay between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)
    
    # Wait for the generated delay
    await asyncio.sleep(delay)
    return delay