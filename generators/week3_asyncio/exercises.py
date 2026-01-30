import asyncio
from typing import Callable


async def async_sleep_and_return(n: int) -> int:
    await asyncio.sleep(0)
    return n


async def run_concurrent(coros, limit=10):
    sem = asyncio.Semaphore(limit)

    async def worker(c):
        async with sem:
            return await c

    return await asyncio.gather(*(worker(c) for c in coros))


# 简单限速器实现
class AsyncRateLimiter:
    def __init__(self, rate: int):
        self._sem = asyncio.Semaphore(rate)

    async def __aenter__(self):
        await self._sem.acquire()

    async def __aexit__(self, exc_type, exc, tb):
        self._sem.release()
