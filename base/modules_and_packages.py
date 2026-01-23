# Python 模块与包示例

# 导入模块
import math
import os
from datetime import datetime

# 使用模块中的函数
print(math.sqrt(16))
print(f"Current working directory: {os.getcwd()}")
print(f"Current date and time: {datetime.now()}")

# 自定义模块示例
# 假设有一个名为 my_module.py 的文件，内容如下：
# def add(a, b):
#     return a + b

# 使用自定义模块
# from my_module import add
# print(add(3, 5))

# 自定义模块复杂示例
# 假设 my_module.py 包含以下内容：
# def subtract(a, b):
#     return a - b
#
# 使用自定义模块
# from my_module import subtract
# print(subtract(10, 3))

import basic_syntax

my_person = basic_syntax.person
print(my_person.introduce())