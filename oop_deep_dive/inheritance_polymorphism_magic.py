# 1. 继承：子类可以继承父类的属性和方法
from re import A


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

class Dog(Animal):
    """Dog 类继承自 Animal 类"""
    def speak(self):
        return f"{self.name} 说 汪汪!"

class Cat(Animal):
    """Cat 类继承自 Animal 类"""
    def speak(self):
        return f"{self.name} 说 喵喵!"

# 2. 多态：不同的对象可以响应相同的消息（方法调用）
def make_animal_speak(animal: Animal):
    """这个函数可以接受任何 Animal 的子类对象"""
    print(animal.speak())

# 创建不同类的实例
my_dog = Dog("旺财")
my_cat = Cat("咪咪")

# 演示继承
print(f"我的狗叫 {my_dog.name}")
print(f"我的猫叫 {my_cat.name}")

print("-" * 20)

# 演示多态
print("演示多态性:")
make_animal_speak(my_dog)  # 传入 Dog 对象
make_animal_speak(my_cat)  # 传入 Cat 对象

print("-" * 20)

# 3. 魔术方法示例: __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """定义当对象被打印时的输出"""
        return f"《{self.title}》 by {self.author}"

my_book = Book("Python编程从入门到实践", "Eric Matthes")
print("魔术方法 __str__ 示例:")
print(my_book)  # 这里会自动调用 my_book.__str__()
