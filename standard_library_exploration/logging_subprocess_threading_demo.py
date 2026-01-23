"""
详细演示：logging, subprocess, threading

本模块展示三个常用模块的基本用法：

- logging: 提供灵活的日志记录功能，支持不同的日志级别、处理器和格式化器，用于将运行时信息记录到控制台或文件。
- subprocess: 用来创建新进程、运行外部命令并与之交互，支持捕获标准输出/错误以及设置超时等选项。
- threading: 提供线程支持，用于并发执行 I/O 密集或短任务（注意 GIL 对 CPU 密集型任务的限制）。

下面的 demo 函数演示如何配置日志、捕获子进程输出以及创建和管理线程。
"""

import logging
import subprocess
import sys
import threading
import time


def demo_logging_config():
    print("--- logging 配置示例 ---")
    logger = logging.getLogger('example')
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug('调试信息')
    logger.info('普通信息')
    logger.error('错误信息示例')


def demo_subprocess_capture():
    print("--- subprocess 捕获输出示例 ---")
    try:
        r = subprocess.run([sys.executable, '-c', 'print("hello from subprocess")'], capture_output=True, text=True)
        print('stdout:', r.stdout.strip())
    except Exception as e:
        print('subprocess 调用失败:', e)


def demo_threading_basic():
    print("--- threading 基础示例 ---")
    def worker(name, delay):
        for i in range(2):
            print(f"线程 {name} 第 {i} 次运行")
            time.sleep(delay)
    t1 = threading.Thread(target=worker, args=("A", 0.01))
    t2 = threading.Thread(target=worker, args=("B", 0.02))
    t1.start(); t2.start()
    t1.join(); t2.join()


if __name__ == "__main__":
    demo_logging_config()
    demo_subprocess_capture()
    demo_threading_basic()
