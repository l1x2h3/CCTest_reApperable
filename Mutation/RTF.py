import ast
import astor

class ReplaceIfCondition(ast.NodeTransformer):
    def visit_If(self, node):
        if isinstance(node.test, ast.Name):
            var_name = node.test.id
            new_test = ast.Compare(
                left=node.test,
                ops=[ast.Eq()],
                comparators=[ast.Compare(
                    left=ast.Name(id=var_name, ctx=ast.Load()),
                    ops=[ast.Eq()],
                    comparators=[ast.Name(id=var_name, ctx=ast.Load())]
                )]
            )
            node.test = new_test
        return node

class ReplaceAddAssign(ast.NodeTransformer):
    def visit_AugAssign(self, node):
        if isinstance(node.op, ast.Add):
            new_node = ast.Assign(
                targets=[node.target],
                value=ast.BinOp(
                    left=node.target,
                    op=ast.Add(),
                    right=node.value
                )
            )
            return new_node
        return node

def replace_add_assign_and_if_condition(code):
    tree = ast.parse(code)
    tree = ReplaceAddAssign().visit(tree)
    tree = ReplaceIfCondition().visit(tree)
    return astor.to_source(tree)

# 示例输入代码
input_code = """
a = 10
b = 5
a += b
if b:
    return a
"""

# 替换 += 操作符和 if 条件
output_code = replace_add_assign_and_if_condition(input_code)
print(output_code)