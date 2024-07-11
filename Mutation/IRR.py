import ast
import astor

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

def replace_add_assign(code):
    tree = ast.parse(code)
    transformer = ReplaceAddAssign()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)

# 示例输入代码
input_code = """
a = 10
b = 5
a += b
print(a)
"""

# 替换 += 操作符
output_code = replace_add_assign(input_code)
print(output_code)