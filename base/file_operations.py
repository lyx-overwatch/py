# Python 文件操作示例

# 写入文件
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# 读取文件
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 追加写入文件
with open("example.txt", "a") as file:
    file.write("\nAppending new content.")

# 逐行读取文件
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 异常处理
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
