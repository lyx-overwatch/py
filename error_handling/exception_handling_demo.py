# 1. 基本的 try...except 结构
try:
    # 尝试执行可能会出错的代码
    result = 10 / 0
    print(f"结果是: {result}")
except ZeroDivisionError as e:
    # 如果发生了特定类型的错误，执行这里的代码
    print(f"捕获到错误: {e}")
    print("不能除以零！")

print("-" * 20)

# 2. 处理多种异常
try:
    user_input = input("请输入一个数字: ")
    number = int(user_input)
    result = 20 / number
    print(f"20 除以 {number} 的结果是 {result}")
except ValueError:
    # 如果用户输入的不是数字，int() 会抛出 ValueError
    print("输入无效，请输入一个有效的数字。")
except ZeroDivisionError:
    # 如果用户输入 0
    print("你输入了 0，不能作为除数。")
except Exception as e:
    # 捕获其他所有意料之外的异常
    print(f"发生了未知错误: {e}")

print("-" * 20)

# 3. try...except...else...finally 结构
def divide(x, y):
    try:
        # 尝试执行除法
        result = x / y
    except ZeroDivisionError:
        print("错误：除数为零！")
    else:
        # 如果 try 块中没有发生异常，则执行 else 块
        print(f"计算成功，结果是: {result}")
    finally:
        # 无论是否发生异常，finally 块中的代码总会被执行
        # 通常用于资源清理，如关闭文件或网络连接
        print("除法操作结束。")

print("调用 divide(10, 2):")
divide(10, 2)
print("\n调用 divide(10, 0):")
divide(10, 0)

print("-" * 20)

# 4. 自定义异常
# 创建一个继承自 Exception 的新异常类
class MyCustomError(Exception):
    """一个自定义的异常类"""
    def __init__(self, message):
        super().__init__(self.message)
        self.message = message
       

def check_age(age):
    if age < 0:
        # 抛出自定义异常
        raise MyCustomError("年龄不能是负数！")
    elif age < 18:
        print("未成年")
    else:
        print("已成年")

try:
    check_age(25)
    check_age(-5)
except MyCustomError as e:
    print(f"捕获到自定义异常: {e}")
