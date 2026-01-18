class MyClass:
    # 类属性
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        # 实例属性
        self.instance_variable = instance_variable

    # 实例方法
    def instance_method(self):
        """可以访问类属性和实例属性"""
        print(f"--- Instance Method ---")
        print(f"Accessing class variable: {self.class_variable}")
        print(f"Accessing instance variable: {self.instance_variable}")

    @classmethod
    def class_method(cls):
        """可以访问类属性，但不能访问实例属性"""
        print(f"\n--- Class Method ---")
        print(f"Accessing class variable: {cls.class_variable}")
        # print(f"Cannot access instance variable: {cls.instance_variable}") # 这会引发 AttributeError

    @staticmethod
    def static_method():
        """不能直接访问类属性或实例属性"""
        print(f"\n--- Static Method ---")
        print("I am a static method. I don't have access to 'cls' or 'self'.")
        # 要访问类属性，需要显式地引用类名
        print(f"Accessing class variable via class name: {MyClass.class_variable}")

# 创建一个实例
my_instance = MyClass("I am an instance variable")

# 调用实例方法
my_instance.instance_method()

# 通过实例调用类方法
my_instance.class_method()

# 通过类调用类方法
MyClass.class_method()

# 通过实例调用静态方法
my_instance.static_method()

# 通过类调用静态方法
MyClass.static_method()
