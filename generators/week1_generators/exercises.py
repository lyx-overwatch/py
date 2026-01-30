from typing import Iterable, Iterator, TypeVar, List, Tuple
from collections import deque

T = TypeVar("T")


def chunked(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    if size < 1:
        raise ValueError("size must be >= 1")
    it = iter(iterable)
    chunk: List[T] = []
    for item in it:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def sliding_window(iterable: Iterable[T], n: int) -> Iterator[Tuple[T, ...]]:
    if n < 1:
        raise ValueError("n must be >= 1")
    it = iter(iterable)
    # use deque with maxlen=n so appending automatically drops the oldest element in O(1)
    window: deque[T] = deque(maxlen=n)
    for _ in range(n):
        try:
            window.append(next(it))
        except StopIteration:
            return
    yield tuple(window)
    for item in it:
        window.append(item)
        yield tuple(window)


def read_lines(path: str) -> Iterator[str]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def words_from_iter(lines: Iterable[str]) -> Iterator[str]:
    for line in lines:
        for word in line.split():
            yield word


def pipeline_filter_map(lines: Iterable[str], predicate, mapper):
    for line in lines:
        if predicate(line):
            yield mapper(line)


if __name__ == "__main__":
    data = range(10)
    print("Chunked:")
    for chunk in chunked(data, 3):
        print(chunk)

    print("\nSliding Window:")
    for window in sliding_window(data, 4):
        print(window);