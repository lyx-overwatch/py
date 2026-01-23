"""
详细演示：itertools 与 functools 的常见用法

本模块展示两个用于函数式编程与迭代器操作的标准库模块：

- itertools: 提供高效的迭代器构造工具（排列、组合、无限迭代、串联、切片等），适合在无须生成完整序列时进行组合操作和流式处理。

- functools: 提供用于函数操作的实用工具，如缓存（lru_cache）、偏函数（partial）、函数组合和降维（reduce）等，常用于性能优化与代码复用。

下面的 demo 函数演示 permutations/combinations、chain/cycle/repeat，以及 lru_cache、partial 和 reduce 的用法示例。
"""

import itertools
from functools import lru_cache, partial, reduce
import operator


def demo_itertools_permutations_combinations():
    print("--- permutations / combinations / combinations_with_replacement ---")
    items = ['a', 'b', 'c']
    print("permutations(2):", list(itertools.permutations(items, 2)))
    print("combinations(2):", list(itertools.combinations(items, 2)))
    print("combinations_with_replacement(2):", list(itertools.combinations_with_replacement(items, 2)))


def demo_itertools_chain_cycle_repeat():
    print("--- chain / cycle / repeat ---")
    print("chain:", list(itertools.chain([1,2], [3,4])))
    print("cycle (first 6):", [x for _, x in zip(range(6), itertools.cycle(["X","Y"]))])
    print("repeat:", [x for x in itertools.islice(itertools.repeat('A', 3), 3)])


def demo_functools_lru_cache_partial_reduce():
    print("--- functools.lru_cache / partial / reduce ---")

    @lru_cache(maxsize=64)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    print("fib(20):", fib(20))

    int_hex = partial(int, base=16)
    print("'ff' ->", int_hex('ff'))

    # reduce 示例：计算乘积
    nums = [1,2,3,4]
    print("乘积:", reduce(operator.mul, nums, 1))


if __name__ == "__main__":
    demo_itertools_permutations_combinations()
    demo_itertools_chain_cycle_repeat()
    demo_functools_lru_cache_partial_reduce()
