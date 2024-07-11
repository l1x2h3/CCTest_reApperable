import requests
import json

# 设置API端点和请求头
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {'sk-7784188a8332407a8280344da079c011'}"
}

# 设置请求数据
data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    "stream": False
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应
print(response.status_code)
print(response.json())