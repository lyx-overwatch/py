# Python 的标准库非常强大，这里我们看几个 `collections` 模块中的例子

# 1. `collections.Counter`: 一个用于计数的字典子类
from collections import Counter

# 统计列表中元素的出现次数
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counts = Counter(my_list)

print("--- collections.Counter 示例 ---")
print(f"原始列表: {my_list}")
print(f"水果计数结果: {fruit_counts}")

# Counter 对象就像一个字典
print(f"苹果的数量: {fruit_counts['apple']}")
print(f"西瓜的数量 (不存在): {fruit_counts['watermelon']}") # 不会报错，返回 0

# most_common() 方法可以找出最常见的元素
print(f"最常见的2种水果: {fruit_counts.most_common(2)}")
print("-" * 20)


# 2. `collections.defaultdict`: 带有默认值的字典
from collections import defaultdict

# 假设我们想按首字母对单词进行分组
words = ['apple', 'ant', 'ball', 'bat', 'cat', 'car']

# 使用普通字典，需要检查 key 是否存在
grouped_words = {}
for word in words:
    first_letter = word[0]
    if first_letter not in grouped_words:
        grouped_words[first_letter] = []
    grouped_words[first_letter].append(word)
print("--- 普通字典分组 ---")
print(grouped_words)

try:
    print(f"访问一个不存在的 key 'z': {grouped_words['z']}") # 会报错
except KeyError as e:
    print(f"访问不存在的 key 报错: {e}")

# 使用 defaultdict，代码更简洁
# 我们告诉 defaultdict，如果一个 key 不存在，就用 list() 创建一个空列表作为默认值
grouped_words_default = defaultdict(list)
print(grouped_words_default)
for word in words:
    grouped_words_default[word[0]].append(word)
print("\n--- collections.defaultdict 分组 ---")
print(grouped_words_default)
print(f"访问一个不存在的 key 'z': {grouped_words_default['z']}") # 不会报错，返回一个空列表
print("-" * 20)


# 3. `collections.namedtuple`: 创建带有命名字段的元组子类
from collections import namedtuple

# 创建一个名为 "Point" 的 namedtuple，它有两个字段 'x' 和 'y'
Point = namedtuple('Point', ['x', 'y'])

# 创建 Point 的实例
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

print("--- collections.namedtuple 示例 ---")
print(f"点 p1: {p1}")
print(f"点 p2: {p2}")

# 可以像访问对象属性一样访问元组的元素
print(f"p1 的 x 坐标: {p1.x}")
print(f"p2 的 y 坐标: {p2.y}")

# 也可以像普通元组一样使用索引
print(f"p1 的第一个元素: {p1[0]}")
print("-" * 20)

# 4. `json` 模块: 用于处理 JSON 数据
import json

# a) 将 Python 字典转换为 JSON 字符串 (序列化)
person_dict = {
    "name": "小明",
    "age": 25,
    "isStudent": False,
    "courses": ["Math", "Science"]
}
# ensure_ascii=False 保证中文字符正常显示
json_string = json.dumps(person_dict, indent=4, ensure_ascii=False)
print("--- json.dumps 示例 ---")
print("Python 字典:")
print(person_dict)
print("\n转换后的 JSON 字符串:")
print(json_string)

# b) 将 JSON 字符串转换回 Python 字典 (反序列化)
json_data = '{"name": "小红", "city": "上海"}'
person_data = json.loads(json_data)
print("\n--- json.loads 示例 ---")
print("原始 JSON 字符串:", json_data)
print("转换后的 Python 字典:", person_data)
print(f"姓名: {person_data['name']}")
