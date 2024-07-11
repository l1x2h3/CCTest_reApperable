import subprocess
import os

def run_bandit(file_path):
    result = subprocess.run(['bandit', '-r', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return result.stdout

def analyze_security(file_path):
    output = run_bandit(file_path)
    # 解析Bandit输出，提取关键信息
    # 例如，提取安全问题数等
    issues = extract_issues(output)
    return issues

def extract_issues(output):
    # 解析Bandit输出，提取安全问题数
    # 示例：[bandit] Test results: 3 issues found
    lines = output.split('\n')
    for line in lines:
        if 'issues found' in line:
            issues = int(line.split()[2])
            return issues
    return 0

def process_folder_security(folder_path, results):
    for i in range(1, 31):
        file_name = f"{i:02d}.py"
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            issues = analyze_security(file_path)
            results.append({
                'file': file_name,
                'issues': issues
            })

def save_results_security(results, output_file):
    with open(output_file, 'w') as f:
        f.write("File\tIssues\n")
        for result in results:
            f.write(f"{result['file']}\t{result['issues']}\n")

def main():
    test1_folder = '../test1'
    result1_folder = '../result1'
    output_file = 'security_result.txt'
    results = []

    process_folder_security(test1_folder, results)
    process_folder_security(result1_folder, results)

    save_results_security(results, output_file)

    # 打印结果
    for result in results:
        print(f"File: {result['file']}, Issues: {result['issues']}")

if __name__ == "__main__":
    main()