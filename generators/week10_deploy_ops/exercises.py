# 示例 Dockerfile 和 docker-compose 内容在 README 中说明。本文件用于提供辅助函数

def docker_run_cmd(image: str, port: int = 8000) -> str:
    return f"docker run -p {port}:8000 {image}"
