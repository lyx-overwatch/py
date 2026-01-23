"""
详细演示：urllib.request 与 statistics

本模块演示两个常见用途：

- urllib.request: 提供发起 HTTP 请求的基础工具，适用于简单的网络访问、下载或与 HTTP 服务交互（注意：在无网络或受限环境中可能无法连接）。

- statistics: 提供基本的统计函数（均值、中位数、标准差等），便于对小规模数据集合进行描述性统计分析。

下面的 demo 演示如何进行一个简单的 GET 请求并解析 JSON，以及如何计算常见统计量。
"""

import urllib.request
import json
import statistics


def demo_urllib_get_json():
    print('--- urllib GET JSON 示例 ---')
    url = 'https://httpbin.org/get'
    try:
        with urllib.request.urlopen(url, timeout=3) as resp:
            text = resp.read().decode('utf-8')
            data = json.loads(text)
            print('origin:', data.get('origin'))
    except Exception as e:
        print('网络请求失败:', e)


def demo_statistics_basic():
    print('--- statistics 示例 ---')
    data = [1,2,2,3,4,10]
    print('mean:', statistics.mean(data))
    print('median:', statistics.median(data))
    print('stdev:', statistics.stdev(data))


if __name__ == '__main__':
    demo_urllib_get_json()
    demo_statistics_basic()
