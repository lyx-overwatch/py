目标

- 掌握并发与并行的模式：threading、multiprocessing、concurrent.futures

练习题

1. 使用 ThreadPoolExecutor 实现并发下载（模拟 IO，使用 sleep）。
2. 使用 ProcessPoolExecutor 实现并行计算（CPU 密集型示例，如大素数判断或斐波那契）。
3. 比较并发与并行在不同任务上的性能差异并记录结果。

交付物

- exercises.py：包含示例函数
- tests：基础测试以确保接口正确
