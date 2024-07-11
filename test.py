import os
from Mutation.INI import insert_print_statement
from Mutation.GRA import insert_garbage_code
from Mutation.IRR import replace_add_assign
from Mutation.REL_R import rename_local_variable
from Mutation.REP_R import rename_parameter
from Mutation.RTF import replace_add_assign_and_if_condition
from NewMutation.func_body import inline_functions
from NewMutation.for_to_while import convert_for_to_while

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    # INI
    transformed_code = insert_print_statement(code)
    # GRA
    transformed_code = insert_garbage_code(transformed_code)
    # IRR
    transformed_code = replace_add_assign(transformed_code)
    # REL_R
    transformed_code = rename_local_variable(transformed_code)
    # REP_R
    transformed_code = rename_parameter(transformed_code, 'left', 'new_left')
    # RTF
    transformed_code = replace_add_assign_and_if_condition(transformed_code)

    # newMutation
    transformed_code = convert_for_to_while(transformed_code)
    transformed_code = inline_functions(transformed_code)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transformed_code)


def process_files_in_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, 31):
        input_file = os.path.join(input_dir, f'{i:02d}.py')
        output_file = os.path.join(output_dir, f'{i:02d}.py')
        if os.path.exists(input_file):
            process_file(input_file, output_file)

# 示例调用
process_files_in_directory('test', 'result')