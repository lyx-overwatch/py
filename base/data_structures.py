# Python 数据结构示例

# 列表
# my_list = [1, 2, 3, 4, 5]
# my_list.append(6)  # 添加元素
# print(my_list)

# # 元组
# my_tuple = (1, 2, 3)
# print(my_tuple[0])  # 访问元素

# # 字典
# my_dict = {"name": "Alice", "age": 25}
# my_dict["city"] = "New York"  # 添加键值对
# print(my_dict)

# # 集合
# my_set = {1, 2, 3}
# my_set.add(4)  # 添加元素
# print(my_set)

# # 嵌套列表
# nested_list = [[1, 2], [3, 4], [5, 6]]
# for sublist in nested_list:
#     for item in sublist:
#         print(item)

# # 字典的复杂操作
# for key, value in my_dict.items():
#     if(key == "age"):
#         my_dict[key] = 10  # 增加年龄

# # 集合操作
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# print(f"Union: {set_a | set_b}")
# print(f"Intersection: {set_a & set_b}")
# print(f"Difference: {set_a - set_b}")

# --- 调试演示代码 ---

def add_and_greet(a, b):
    """一个简单的函数，计算总和并返回一个问候语."""
    print("进入 add_and_greet 函数内部...")
    result = a + b
    greeting = f"计算结果是: {result}"
    print("...即将离开 add_and_greet 函数")
    return greeting

def demonstrate_debugging():
    """主函数，用于演示调试步骤."""
    print("调试演示开始")
    x = 10
    y = 20
    
    # 在下面这一行设置断点
    message = add_and_greet(x, y)
    
    print(message)
    print("调试演示结束")

if __name__ == "__main__":
    demonstrate_debugging()
