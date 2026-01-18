class MyClass:
    # 一个简单的类属性
    my_list = []
    my_name = "I am a class attribute"

print(f"--- Initial State ---")
print(f"Class attribute 'my_name' on MyClass: {MyClass.my_name}")
print("-" * 20)

# 创建第一个实例
instance_one = MyClass()
print(f"instance_one 'my_name': {instance_one.my_name}")

# 通过 instance_one 修改 'my_name'
# 这实际上是在 instance_one 上创建了一个新的实例属性
print("\n--- Modifying 'my_name' via instance_one ---")
instance_one.my_name = "Value modified by instance_one"
print(f"instance_one 'my_name': {instance_one.my_name}")

# 类属性本身没有改变
print(f"Class attribute 'my_name' on MyClass: {MyClass.my_name}")
print("-" * 20)

# 现在创建一个新的实例
print("\n--- Creating a new instance (instance_two) ---")
instance_two = MyClass()

# instance_two 仍然引用原始的类属性
print(f"instance_two 'my_name': {instance_two.my_name}")
print("-" * 20)


print("\n--- What about mutable attributes like lists? ---")
# 所有的实例共享同一个列表对象
instance_one.my_list.append(1)
print(f"instance_one 'my_list': {instance_one.my_list}")
print(f"instance_two 'my_list': {instance_two.my_list}")

# 新的实例也会看到被修改过的列表
instance_three = MyClass()
print(f"instance_three 'my_list': {instance_three.my_list}")
print(f"Class 'my_list': {MyClass.my_list}")
print("\nConclusion: Modifying a mutable class attribute affects all instances.")

