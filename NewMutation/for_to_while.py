import ast
import astor

class ForToWhile(ast.NodeTransformer):
    def visit_For(self, node):
        target = node.target
        iter = node.iter
        body = node.body
        orelse = node.orelse

        # 创建一个新的 while 循环
        while_body = [
            ast.Assign(targets=[target], value=ast.Call(func=ast.Name(id='next', ctx=ast.Load()), args=[iter], keywords=[])),
            ast.If(
                test=ast.Call(func=ast.Name(id='isinstance', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='next', ctx=ast.Load()), args=[iter], keywords=[]), ast.Name(id='StopIteration', ctx=ast.Load())], keywords=[]),
                body=[ast.Break()],
                orelse=body
            )
        ]

        return ast.While(test=ast.Constant(value=True), body=while_body, orelse=orelse)

def convert_for_to_while(code):
    tree = ast.parse(code)
    transformer = ForToWhile()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)

# 示例输入代码
input_code = """
for i in range(5):
    print(i)
"""

# 将 for 循环替换为 while 循环
output_code = convert_for_to_while(input_code)
print(output_code)