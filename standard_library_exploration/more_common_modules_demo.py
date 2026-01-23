# 更多 Python 标准库常用模块示例（每项为独立小示例）
# 说明：这些示例都尽量简短，便于学习和调试。

import os
import sys
from pathlib import Path
import datetime
import time
import itertools
from functools import lru_cache, partial
import heapq
import random
import logging
import subprocess
import threading
import re
import hashlib
import urllib.request
import statistics


def demo_os_pathlib():
    print("--- os / pathlib 示例 ---")
    cwd = os.getcwd()
    print("当前工作目录:", cwd)
    p = Path(cwd) / "example.txt"
    print("Path 拼接示例:", p)


def demo_sys():
    print("--- sys 示例 ---")
    print("Python 可执行文件:", sys.executable)
    print("模块搜索路径示例（前3）:", sys.path[:3])


def demo_datetime_time():
    print("--- datetime / time 示例 ---")
    now = datetime.datetime.now()
    print("现在（datetime）:", now)
    print("格式化时间:", now.strftime('%Y-%m-%d %H:%M:%S'))
    t0 = time.time()
    time.sleep(0.01)
    t1 = time.time()
    print("耗时 (秒):", t1 - t0)


def demo_itertools():
    print("--- itertools 示例 ---")
    a = [1, 2, 3]
    print("permutations 2:", list(itertools.permutations(a, 2)))
    print("combinations 2:", list(itertools.combinations(a, 2)))
    # 无限迭代器示例（只取前 5）
    print("cycle 前5:", [x for _, x in zip(range(5), itertools.cycle(["A", "B"]))])


def demo_functools():
    print("--- functools 示例 ---")

    @lru_cache(maxsize=32)
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print("fib(10):", fib(10))
    # partial 用法
    int_base2 = partial(int, base=2)
    print("'1010' ->", int_base2('1010'))


def demo_heapq():
    print("--- heapq 示例 ---")
    nums = [5, 1, 7, 3, 2]
    heapq.heapify(nums)
    print("heapify 后的最小元素:", nums[0])
    print("按升序弹出所有元素:", [heapq.heappop(nums) for _ in range(len(nums))])


def demo_random():
    print("--- random 示例 ---")
    print("随机选择:", random.choice(["red", "green", "blue"]))
    print("随机样本 3 个:", random.sample(range(10), 3))


def demo_logging():
    print("--- logging 示例 ---")
    logger = logging.getLogger("demo")
    if not logger.handlers:
        h = logging.StreamHandler()
        fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
        h.setFormatter(fmt)
        logger.addHandler(h)
    logger.setLevel(logging.INFO)
    logger.info("这是一条信息日志")
    logger.warning("这是一条警告")


def demo_subprocess():
    print("--- subprocess 示例 ---")
    # 注意：在某些环境下外部命令可能不可用
    try:
        res = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print("Python 版本（通过 subprocess）:", res.stdout.strip() or res.stderr.strip())
    except Exception as e:
        print("subprocess 调用失败:", e)


def demo_threading():
    print("--- threading 示例 ---")
    def worker(n):
        print(f"线程启动: {n}")
        time.sleep(0.01)
        print(f"线程结束: {n}")
    t = threading.Thread(target=worker, args=(1,))
    t.start()
    t.join()


def demo_re_hashlib():
    print("--- re / hashlib 示例 ---")
    s = "Contact: alice@example.com"
    m = re.search(r"[\w.-]+@[\w.-]+", s)
    print("找到邮箱:", m.group(0) if m else None)
    # hashlib
    h = hashlib.sha256(b"hello world").hexdigest()
    print("sha256('hello world'):", h)


def demo_urllib_statistics():
    print("--- urllib.request / statistics 示例 ---")
    # urllib 请求一个简单的 URL（仅在允许外网请求时有效）
    url = "http://httpbin.org/get"
    try:
        with urllib.request.urlopen(url, timeout=2) as resp:
            print("url 状态码:", resp.status)
    except Exception as e:
        print("urllib 请求失败（可能无网络）:", e)
    # statistics
    data = [1, 2, 2, 3, 4]
    print("平均值:", statistics.mean(data))
    print("中位数:", statistics.median(data))


if __name__ == "__main__":
    demo_os_pathlib()
    demo_sys()
    demo_datetime_time()
    demo_itertools()
    demo_functools()
    demo_heapq()
    demo_random()
    demo_logging()
    demo_subprocess()
    demo_threading()
    demo_re_hashlib()
    demo_urllib_statistics()
