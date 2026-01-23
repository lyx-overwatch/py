"""
详细演示：re 与 hashlib

本模块展示两个常用模块的基本用法：

- re: 正则表达式模块，用于在文本中搜索、匹配、提取和替换模式。支持查找所有匹配（findall）、分组（groups）、搜索（search）和替换（sub）等操作，适用于日志、文本解析和数据清洗场景。

- hashlib: 提供加密哈希算法（如 MD5、SHA1、SHA256 等），用于生成消息摘要、校验和、密码存储的散列等用途。

下面的 demo 演示如何使用正则表达式提取邮箱，以及如何使用 hashlib 计算常见哈希值。
"""

import re
import hashlib


def demo_re_findall_groups():
    print("--- re.findall 与 分组 ---")
    text = "My email is test.user@example.com and backup is admin@domain.org"
    emails = re.findall(r"[\w.-]+@[\w.-]+", text)
    print("找到的邮件:", emails)

    # 分组示例
    m = re.search(r"(\w+)@(\w+\.\w+)", "contact: foo@bar.com")
    if m:
        print('user:', m.group(1), 'domain:', m.group(2))


def demo_hashlib_use_cases():
    print("--- hashlib hash 用法 ---")
    s = 'hello world'.encode('utf-8')
    print('md5:', hashlib.md5(s).hexdigest())
    print('sha1:', hashlib.sha1(s).hexdigest())
    print('sha256:', hashlib.sha256(s).hexdigest())


if __name__ == "__main__":
    demo_re_findall_groups()
    demo_hashlib_use_cases()
