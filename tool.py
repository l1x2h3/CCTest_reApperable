import os
import shutil
import requests
import json

# API端点和请求头
API_URL = "https://api.deepseek.com/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-7784188a8332407a8280344da079c011"  # 确保格式正确
}

# 调用代码生成工具
def code_generation_tool(prompt):
    payload = {
        "model": "deepseek-chat",  # 确保包含模型字段
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    print(f"Sending request to: {API_URL}")
    print(f"Headers: {HEADERS}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return ""

# 统计返回值在函数中被调用的次数
global_call_count = 0

def modify_code_with_tool(code):
    global global_call_count
    prompt = f"Modify the following code,you need only give me the code and do not say any other thing:\n{code}"
    modified_code = code_generation_tool(prompt)
    global_call_count += modified_code.count("return")
    return modified_code

def process_files_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, 31):
        input_file = os.path.join(input_folder, f"{i:02d}.py")
        output_file = os.path.join(output_folder, f"{i:02d}.py")

        if os.path.exists(input_file):
            with open(input_file, 'r', encoding='utf-8') as f:
                code = f.read()

            modified_code = modify_code_with_tool(code)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(modified_code)

def main():
    test_folder = 'test'
    test1_folder = 'test1'
    result_folder = 'result'
    result1_folder = 'result1'

    process_files_in_folder(test_folder, test1_folder)
    process_files_in_folder(result_folder, result1_folder)

    print(f"Global call count: {global_call_count}")

if __name__ == "__main__":
    main()