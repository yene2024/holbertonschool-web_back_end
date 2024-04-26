#!/usr/bin/env python3
"""Writing a coroutine called async_generator
that takes no arguments."""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random number between
    0 and 10 after waiting for 1 second,
    repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
