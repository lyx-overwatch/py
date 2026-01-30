目标

- 掌握生成器、迭代器、yield、生成器表达式与惰性流处理

每周时间分配（总计 10 小时）

- 理论学习与阅读 2h
- 实战编码（实现 chunked/sliding_window/流式读取等）6h
- 编写单元测试与文档 1.5h
- 复盘与提交 0.5h

练习题

1. 实现一个 `chunked(iterable, size)`，返回定长分块的生成器（支持最后一块短于 size）。
2. 实现 `sliding_window(iterable, n)`，返回滑动窗口元组的生成器。
3. 实现基于生成器的文件流处理：`read_lines(path)` 按行惰性读取并去除换行符。
4. 使用上面的函数实现分块词数统计，并写 pytest 测试覆盖边界情况。
5. 拓展：实现一个惰性过滤 + map 管道，能够在文件行流上链式处理。

交付物

- 一个包含实现和测试的模块（推荐放到 `generators/week1_generators/exercises.py`）
- README 中写明如何运行测试和示例命令

理论与参考（简明）

什么是生成器与迭代器

- 迭代器（iterator）是实现了 `__iter__()` 和 `__next__()` 的对象，能够按需返回序列的下一个元素。
- 生成器（generator）是用 `yield` 语句定义的函数／表达式，返回一个遵循迭代器协议的惰性可迭代对象。

yield 与惰性求值

- `yield` 会“暂停”函数并返回一个值，下一次调用 `__next__()` 时从暂停处继续。生成器只在需要时才产生值，节省内存。

生成器表达式与列表推导的对比

- 列表推导会立即生成整个列表（占用内存）。生成器表达式使用圆括号，按需生成元素，适合大数据流处理。

常见场景与复杂度

- 流式文件处理：用生成器逐行读取大文件，避免一次性把文件读入内存。
- chunked：按固定大小分块，时间复杂度 O(n)，额外空间为单个块（O(size))。
- sliding_window：维护固定大小滑窗，时间复杂度 O(n)，空间 O(n)（n 为窗口大小）。

边界情况

- size 或 n 小于 1 应抛出 ValueError（示例实现如此处理）。
- 空输入应能正确返回空的生成器而不抛出意外异常。

如何运行测试

- 在项目根目录（包含 `generators` 文件夹的上级目录）运行：

  pytest -q

- 在 Windows 的 bash（例如 Git Bash）中命令相同。

参考链接

- 官方文档：[generator types](https://docs.python.org/3/library/stdtypes.html#generator-types)
- 迭代器协议与 PEP：[PEP 234](https://peps.python.org/pep-0234/)

示例练习建议

- 为每个函数增加 docstring 和类型注解（已在代码中提供）。
- 添加更多单元测试覆盖边界（size=1、size>len、n>len、无效参数等）。
