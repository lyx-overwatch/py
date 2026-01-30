# Python 面向对象编程示例

# 定义类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
    
    def eat(self):
        print(f"{self.name} is eating")
    
    @staticmethod
    def info():
        print("Animals are living beings.")

# 继承
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# 多态
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

animals = [Dog("Buddy"), Cat("Kitty")]
for animal in animals:
    animal.speak()

# 类方法和静态方法
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(3, 5))
print(MathUtils.multiply(3, 5))
