import os

def comment_out_first_and_last_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if lines:
        lines[0] = f"# {lines[0]}"  # 注释第一行
        lines[-1] = f"# {lines[-1]}"  # 注释最后一行

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def process_folder(folder_path):
    for i in range(1, 31):
        file_name = f"{i:02d}.py"
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            comment_out_first_and_last_line(file_path)
            print(f"Processed {file_path}")

def main():
    test1_folder = 'test1'
    result1_folder = 'result1'

    process_folder(test1_folder)
    process_folder(result1_folder)

if __name__ == "__main__":
    main()