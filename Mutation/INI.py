import ast
import astor

class InsertPrintStatement(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        # 在函数体的任意位置插入 print 语句
        used_vars = self.find_used_vars(node)
        if used_vars:
            var_name = used_vars[0]
            insert_index = self.find_insert_index(node, var_name)
            if insert_index is not None:
                print_statement = ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id='print', ctx=ast.Load()),
                        args=[ast.Name(id=var_name, ctx=ast.Load())],
                        keywords=[]
                    )
                )
                # 选择一个位置插入 print 语句，这里选择在变量出现之后的第一个位置
                node.body.insert(insert_index + 1, print_statement)
        return node

    def find_used_vars(self, node):
        # 找到在当前节点之前定义的变量
        used_vars = []
        for child in node.body:
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Name):
                        used_vars.append(target.id)
        return used_vars

    def find_insert_index(self, node, var_name):
        # 找到变量出现的第一个位置
        for i, child in enumerate(node.body):
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Name) and target.id == var_name:
                        return i
        return None

def insert_print_statement(code):
    tree = ast.parse(code)
    transformer = InsertPrintStatement()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)

# 示例输入代码
input_code = """
def add(a, b):
    res = a + b
    if a > b:
        return res
"""

# 插入 print 语句
output_code = insert_print_statement(input_code)
print(output_code)