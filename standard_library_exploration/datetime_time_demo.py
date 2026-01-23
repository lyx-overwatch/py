"""
详细演示：datetime 和 time 模块

本模块展示 Python 标准库中与日期/时间相关的两个常用模块：

- datetime: 提供日期、时间和时区的高级表示与操作。常用类有 date, time, datetime, timedelta, timezone。
  适用于日期时间的解析、格式化、时区处理与算术运算（加减时间间隔）。

- time: 提供底层时间功能与计时器，如获取时间戳、睡眠和高精度计时（perf_counter）。
  常用于延迟、性能测量以及与系统时间戳交互。

下面的 demo 函数演示如何获取当前时间、格式化/解析字符串、使用时区以及用高精度计时器测量耗时。
"""

import datetime
import time


def demo_now_and_formatting():
    print("--- datetime.now 与格式化 ---")
    now = datetime.datetime.now()
    print("现在:", now)
    print("ISO 格式:", now.isoformat())
    print("自定义格式:", now.strftime('%Y-%m-%d %H:%M:%S'))


def demo_parsing():
    print("--- 字符串解析为 datetime ---")
    s = "2024-08-15 13:45:30"
    dt = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    print("解析结果:", dt, type(dt))


def demo_timezone():
    print("--- 时区示例 (datetime.timezone) ---")
    tz_utc = datetime.timezone.utc
    now_utc = datetime.datetime.now(tz=tz_utc)
    print("UTC 时间:", now_utc)


def demo_sleep_and_perf():
    print("--- time.sleep 与 perf_counter ---")
    t0 = time.perf_counter()
    time.sleep(0.02)
    t1 = time.perf_counter()
    print("高精度耗时:", t1 - t0)


if __name__ == "__main__":
    demo_now_and_formatting()
    demo_parsing()
    demo_timezone()
    demo_sleep_and_perf()
