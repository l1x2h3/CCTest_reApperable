import ast
import astor

class FunctionInlining(ast.NodeTransformer):
    def __init__(self):
        self.function_defs = {}

    def visit_FunctionDef(self, node):
        self.function_defs[node.name] = node
        return node

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id in self.function_defs:
            function_def = self.function_defs[node.value.func.id]
            new_body = []
            for stmt in function_def.body:
                if isinstance(stmt, ast.Return):
                    new_body.append(ast.Assign(targets=[ast.Name(id='_result', ctx=ast.Store())], value=stmt.value))
                else:
                    new_body.append(stmt)
            new_body.append(ast.Assign(targets=node.targets, value=ast.Name(id='_result', ctx=ast.Load())))
            return ast.fix_missing_locations(ast.Module(body=new_body, type_ignores=[]))
        return node

def inline_functions(code):
    tree = ast.parse(code)
    transformer = FunctionInlining()
    new_tree = transformer.visit(tree)
    return astor.to_source(new_tree)

# 示例输入代码
input_code = """
def add(a, b):
    return a + b

result = add(1, 2)
"""

# 内联函数
output_code = inline_functions(input_code)
print(output_code)