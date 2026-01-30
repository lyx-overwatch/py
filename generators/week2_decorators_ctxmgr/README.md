目标
- 掌握装饰器（含参数化、保留函数元信息）与上下文管理器

练习题
1. 实现一个 `timing` 装饰器，记录函数执行时长并可选记录到日志。
2. 实现一个 `retry` 装饰器，支持重试次数与延迟策略。
3. 使用 `contextlib` 实现自定义上下文管理器 `temporary_file(contents)`，在上下文中返回文件路径并在退出时删除。

交付物
- `exercises.py` 中包含实现
- `tests/test_exercises.py` 包含对应 pytest 测试
