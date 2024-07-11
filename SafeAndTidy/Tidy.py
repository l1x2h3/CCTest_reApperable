import subprocess
import os
import re

def run_pylint(file_path):
    result = subprocess.run(['pylint', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return result.stdout

def analyze_code(file_path):
    output = run_pylint(file_path)
    # 解析Pylint输出，提取关键信息
    # 例如，提取评分、错误数、警告数等
    score = extract_score(output)
    errors = extract_errors(output)
    warnings = extract_warnings(output)
    return score, errors, warnings

def extract_score(output):
    # 解析Pylint输出，提取评分
    # 示例：Your code has been rated at 10.00/10
    lines = output.split('\n')
    for line in lines:
        if 'rated at' in line:
            score = float(line.split()[6].split('/')[0])
            print(score)
            return score
    return None

def extract_errors(output):
    # 解析Pylint输出，提取错误数
    error_pattern = re.compile(r'\b[CE]\d{3}\b')  # 匹配错误和致命错误代码
    errors = error_pattern.findall(output)
    return len(errors)

def extract_warnings(output):
    # 解析Pylint输出，提取警告数
    warning_pattern = re.compile(r'\bW\d{3}\b')  # 匹配警告代码
    warnings = warning_pattern.findall(output)
    return len(warnings)

def process_folder(folder_path, results):
    for i in range(1, 31):
        file_name = f"{i:02d}.py"
        file_path = os.path.join(folder_path, file_name)
        print(file_name)
        if os.path.exists(file_path):
            print("yes")
            score, errors, warnings = analyze_code(file_path)
            results.append({
                'file': file_name,
                'score': score,
                'errors': errors,
                'warnings': warnings
            })

def save_results(results, output_file):
    with open(output_file, 'w') as f:
        f.write("File\tScore\tErrors\tWarnings\n")
        for result in results:
            f.write(f"{result['file']}\t{result['score']}\t{result['errors']}\t{result['warnings']}\n")

def main():
    test1_folder = '../test1'
    result1_folder = '../result1'
    output_file = 'result.txt'
    results = []

    process_folder(test1_folder, results)
    process_folder(result1_folder, results)

    save_results(results, output_file)

    # 打印结果
    for result in results:
        print(f"File: {result['file']}, Score: {result['score']}, Errors: {result['errors']}, Warnings: {result['warnings']}")

if __name__ == "__main__":
    main()