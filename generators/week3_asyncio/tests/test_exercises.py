import asyncio

from generators.week3_asyncio.exercises import async_sleep_and_return, run_concurrent, AsyncRateLimiter


def test_async_sleep_and_return():
    res = asyncio.run(async_sleep_and_return(1))
    assert res == 1


def test_run_concurrent():
    coros = [async_sleep_and_return(i) for i in range(5)]
    res = asyncio.run(run_concurrent(coros, limit=2))
    assert res == [0,1,2,3,4]


def test_async_rate_limiter():
    async def worker(limiter):
        async with limiter:
            await asyncio.sleep(0)
            return True

    limiter = AsyncRateLimiter(rate=2)
    res = asyncio.run(asyncio.gather(*(worker(limiter) for _ in range(3))))
    assert all(res)
