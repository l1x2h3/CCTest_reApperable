import ast
import astor

class InsertGarbageCode(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        # 在函数体的任意位置插入垃圾代码
        used_vars = self.find_used_vars(node)
        if used_vars:
            garbage_code = ast.If(
                test=ast.Constant(value=False),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id='TempVar', ctx=ast.Store())],
                        value=ast.Name(id=used_vars[0], ctx=ast.Load())
                    )
                ],
                orelse=[]
            )
            # 选择一个位置插入垃圾代码，这里选择在函数体的第一个位置
            node.body.insert(0, garbage_code)
        return node

    def visit_If(self, node):
        # 在 if 语句的任意位置插入垃圾代码
        used_vars = self.find_used_vars(node)
        if used_vars:
            garbage_code = ast.If(
                test=ast.Constant(value=False),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id='TempVar', ctx=ast.Store())],
                        value=ast.Name(id=used_vars[0], ctx=ast.Load())
                    )
                ],
                orelse=[]
            )
            # 选择一个位置插入垃圾代码，这里选择在 if 语句的第一个位置
            node.body.insert(0, garbage_code)
        return node

    def find_used_vars(self, node):
        # 找到在当前节点之前定义的变量
        used_vars = set()
        parent = self.parent_node(node)
        if parent:
            for child in parent.body:
                if isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            used_vars.add(target.id)
                if child == node:
                    break
        return list(used_vars)

    def parent_node(self, node):
        # 找到当前节点的父节点
        for parent in ast.walk(self.tree):
            for child in ast.iter_child_nodes(parent):
                if child == node:
                    return parent
        return None

def insert_garbage_code(code):
    tree = ast.parse(code)
    transformer = InsertGarbageCode()
    transformer.tree = tree
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)

# 示例输入代码
input_code = """
def add(a, b):
    res = a + b
    if a > b:
        return res
"""

# 插入垃圾代码
output_code = insert_garbage_code(input_code)
print(output_code)