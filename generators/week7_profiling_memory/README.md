目标

- 掌握性能剖析工具：cProfile、line_profiler、memory_profiler 等

练习题

1. 使用 cProfile 对一个函数进行剖析并解析输出。
2. 使用 memory_profiler 测试内存使用峰值。
3. 找出热点并进行优化（如避免重复计算、使用局部变量等）。

交付物

- exercises.py 包含一个可剖析的示例函数
- tests/ 中包含运行时调用（不需要真实 profiler 环境）
