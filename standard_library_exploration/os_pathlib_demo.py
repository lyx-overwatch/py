"""
详细演示：os 与 pathlib 的常见用法
说明：两个模块经常交替使用，pathlib 提供面向对象的路径操作，os 提供更底层的系统接口。

本模块将展示如何使用 Path 创建/检查路径、遍历和 glob、以及使用 os 和 shutil 进行文件操作（重命名/移动/删除/权限修改）。
"""

import os
from pathlib import Path
import shutil
import stat


def demo_path_creation_and_inspection():
    print("--- Path 创建与检查 ---")
    p = Path.cwd() / "demo_dir"
    print("目标路径:", p)

    # 创建目录（存在时不报错）
    p.mkdir(parents=True, exist_ok=True)
    print("已创建目录(如果之前不存在)")

    # 创建子文件并写入
    file_path = p / "sample.txt"
    file_path.write_text("Hello Pathlib\n", encoding="utf-8")
    print("已写入文件:", file_path)

    # 检查类型
    print("是否是文件:", file_path.is_file())
    print("是否是目录:", p.is_dir())

    # 获取文件信息
    stat_info = file_path.stat()
    print("文件大小:", stat_info.st_size)


def demo_traversal_and_glob():
    print("--- 遍历与模式匹配 (glob) ---")
    base = Path.cwd()
    # 查找当前目录下的 py 文件
    for f in base.glob("*.py"):
        print("发现 py 文件:", f.name)


def demo_os_file_ops():
    print("--- os 低级文件操作 ---")
    # 重命名/移动
    src = Path.cwd() / "os_pathlib_demo_temp.txt"
    dst = Path.cwd() / "os_pathlib_demo_temp_renamed.txt"
    src.write_text("temp\n", encoding="utf-8")
    print("创建临时文件", src.name)
    os.replace(src, dst)
    print(f"已移动/重命名为 {dst.name}")

    # 权限修改 (仅演示，不改变核心权限)
    try:
        # 设置为可读写
        os.chmod(dst, stat.S_IREAD | stat.S_IWRITE)
        print("修改了文件权限 (示例)")
    except Exception as e:
        print("修改权限失败:", e)

    # 删除示例
    try:
        dst.unlink()
        print("已删除示例文件", dst.name)
    except Exception as e:
        print("删除文件失败:", e)


def demo_copy_move_remove():
    print("--- 文件复制/移动/删除 (shutil) ---")
    src_dir = Path.cwd() / "demo_dir"
    src_file = src_dir / "sample.txt"
    copy_file = Path.cwd() / "copy_of_sample.txt"
    shutil.copy2(src_file, copy_file)
    print("已复制文件到", copy_file)

    # 移动到新的目录
    target_dir = Path.cwd() / "demo_dir_moved"
    target_dir.mkdir(exist_ok=True)
    shutil.move(str(src_dir), str(target_dir / src_dir.name))
    print("已移动目录到", target_dir)

    # 清理：删除复制的文件和移动的目录
    try:
        copy_file.unlink()
        shutil.rmtree(target_dir)
        print("已清理临时文件与目录")
    except Exception as e:
        print("清理失败:", e)


if __name__ == "__main__":
    demo_path_creation_and_inspection()
    demo_traversal_and_glob()
    demo_os_file_ops()
    demo_copy_move_remove()
