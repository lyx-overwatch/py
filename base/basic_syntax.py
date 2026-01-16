# Python 基本语法示例

# 变量与数据类型
a = 10  # 整数
b = 3.14  # 浮点数
c = "Hello, Python!"  # 字符串
d = True  # 布尔值

# 条件语句
if a > 5:
    print("a is greater than 5")
else:
    print("a is less than or equal to 5")

# 循环
for i in range(5):
    print(f"Iteration {i}")

while a > 0:
    print(a)
    a -= 1

# 函数
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 类与对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Alice", 30)
print(person.introduce())

# 更多数据类型
# None 类型
e = None
print(f"e is of type {type(e)}")

# 复杂条件语句
if a > 5 and b < 10:
    print("a is greater than 5 and b is less than 10")
elif c == "Hello, Python!":
    print("c matches the expected string")
else:
    print("None of the conditions matched")

# 嵌套循环
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
