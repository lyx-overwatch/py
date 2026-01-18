# 1. Lambda 表达式：一种快速定义单行匿名函数的方式
# 传统函数定义
def square(x):
    return x * x

# 使用 lambda 表达式
square_lambda = lambda x: x * x

print(f"传统函数计算 5 的平方: {square(5)}")
print(f"Lambda 表达式计算 5 的平方: {square_lambda(5)}")
print("-" * 20)


# 2. 高阶函数：可以接受函数作为参数或返回函数的函数

# a) map(): 将一个函数应用于一个序列的所有元素
numbers = [1, 2, 3, 4, 5]
# 使用 map 和 lambda 来计算列表中每个数字的平方
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"使用 map() 将 {numbers} 中的每个元素平方: {squared_numbers}")
print("-" * 20)


# b) filter(): 使用一个函数来过滤序列，只保留返回 True 的元素
# 使用 filter 和 lambda 来筛选出列表中的偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"使用 filter() 从 {numbers} 中筛选出偶数: {even_numbers}")
print("-" * 20)


# 3. 列表推导式：一种更简洁、更具 Python 特色的创建列表的方式
# 使用 for 循环创建平方列表
squared_numbers_loop = []
for num in numbers:
    squared_numbers_loop.append(num * num)

# 使用列表推导式达到同样的效果
squared_numbers_comprehension = [num * num for num in numbers]

print(f"For 循环创建的平方列表: {squared_numbers_loop}")
print(f"列表推导式创建的平方列表: {squared_numbers_comprehension}")

# 带条件的列表推导式：只对偶数进行平方
squared_even_numbers = [num * num for num in numbers if num % 2 == 0]
print(f"列表推导式只对偶数平方: {squared_even_numbers}")
print("-" * 20)


# 4. 生成器表达式：类似于列表推导式，但它返回一个生成器对象，更节省内存
# 生成器表达式使用圆括号 ()
squared_numbers_generator = (num * num for num in numbers)
print(f"这是一个生成器对象: {squared_numbers_generator}")
print("我们可以迭代它来获取值:")
for val in squared_numbers_generator:
    print(val, end=" ")
print()
