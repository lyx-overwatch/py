"""
详细演示：heapq 与 random

本模块演示 Python 标准库中两个模块的常见用法：

- heapq: 提供堆队列算法（最小堆实现），适用于快速获取最小/最大元素、维护大小受限的优先队列等。
  常用函数：heapify、heappush、heappop、nlargest、nsmallest、heappushpop、heapreplace。

- random: 提供伪随机数工具，用于生成随机数、随机抽样、打乱序列、设置随机种子等。
  常用函数：random、randint、choice、sample、choices、shuffle、seed。

下面的 demo 示例展示如何分别使用 heapq（例如获取 top-n、维护堆）和 random（打乱、抽样、设置种子）。
"""

import heapq
import random


def demo_heapq_top_n():
    print("--- heapq top n 示例 ---")
    data = [random.randint(1,100) for _ in range(10)]
    print("原始数据:", data)
    print("最大 3 个:", heapq.nlargest(3, data))
    print("最小 3 个:", heapq.nsmallest(3, data))


def demo_heapq_pushpop():
    print("--- heapq pushpop / replace ---")
    h = []
    for v in [5,1,3]:
        heapq.heappush(h, v)
    print("heap:", h)
    print("heappushpop 2 ->", heapq.heappushpop(h, 2))


def demo_random_choices_shuffle():
    print("--- random choices / shuffle / seed ---")
    items = list(range(10))
    random.seed(0)
    random.shuffle(items)
    print("shuffle 后:", items)
    print("choices (有放回):", random.choices(items, k=5))
    print("sample (无放回):", random.sample(items, 3))


if __name__ == "__main__":
    demo_heapq_top_n()
    demo_heapq_pushpop()
    demo_random_choices_shuffle()
