import os
import subprocess

def run_script(script_path):
    result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # print("OK")
    return result.returncode, result.stdout.strip()

def compare_scripts(result_script, test_script):
    result_returncode, result_output = run_script(result_script)
    test_returncode, test_output = run_script(test_script)

    if result_returncode == test_returncode and result_output == test_output:
        return True
    else:
        return False

def main():
    result_folder = 'result'
    test_folder = 'test'
    num_scripts = 30
    correct_count = 0

    for i in range(1, num_scripts + 1):
        result_script = os.path.join(result_folder, f'{i:02d}.py')
        test_script = os.path.join(test_folder, f'{i:02d}.py')

        if not os.path.exists(result_script) or not os.path.exists(test_script):
            print(f'Error: Script {i:02d}.py does not exist in one of the folders.')
            continue

        if compare_scripts(result_script, test_script):
            print(f'Script {i:02d}.py: pass')
            correct_count += 1
        else:
            print(f'Script {i:02d}.py: error')

    print(f'Total correct scripts: {correct_count}')

if __name__ == '__main__':
    main()