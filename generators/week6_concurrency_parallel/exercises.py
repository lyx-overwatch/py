import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List


def simulate_io(n: int, delay: float = 0.01) -> int:
    time.sleep(delay)
    return n


def run_thread_pool(values: List[int], workers: int = 5) -> List[int]:
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(simulate_io, values))


def fib(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def run_process_pool(values: List[int], workers: int = 2) -> List[int]:
    with ProcessPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(fib, values))
