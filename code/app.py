import time
import subprocess  

import redis
from flask import Flask, render_template, request
app = Flask(__name__)

# 启用调试模式
if __name__ == '__main__':
    app.run(debug=True)

cache = redis.Redis(host='redis', port=6379)

# 执行 shell 命令  
def get_fortune():
    result = subprocess.run(['/usr/games/fortune'], capture_output=True, text=True)
    # 检查是否有错误  
    if result.returncode != 0:
        return f"Error occurred: {result.stderr}"
    else:
        return result.stdout

# 利用 Redis 缓存机制实现计数器
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# 调用模板渲染功能生成网页
@app.route('/')
def fortune():
    fortune = get_fortune()
    count = get_hit_count()
    return render_template("poet.html",fortune=fortune,hits=count)