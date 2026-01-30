import time
from functools import wraps
from contextlib import contextmanager
from typing import Callable, Any


def timing(log_fn: Callable[[str], None] | None = None):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.perf_counter()
                msg = f"{func.__name__} took {end - start:.6f}s"
                if log_fn:
                    log_fn(msg)
                else:
                    print(msg)

        return wrapper

    return decorator


def retry(times: int = 3, delay: float = 0.0):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if delay:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


@contextmanager
def temporary_file(contents: str):
    import tempfile
    import os

    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contents)
        yield path
    finally:
        try:
            os.remove(path)
        except OSError:
            pass
