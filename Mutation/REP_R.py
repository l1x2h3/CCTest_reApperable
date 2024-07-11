import ast
import astor


class ParameterRenamer(ast.NodeTransformer):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def visit_FunctionDef(self, node):
        # Rename parameters in the function definition
        for i, arg in enumerate(node.args.args):
            if arg.arg == self.old_name:
                node.args.args[i].arg = self.new_name

        # Continue visiting child nodes
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        # Rename occurrences of the parameter within the function body
        if isinstance(node.ctx, ast.Load) and node.id == self.old_name:
            node.id = self.new_name
        return node


def rename_parameter(code, old_name, new_name):
    tree = ast.parse(code)
    renamer = ParameterRenamer(old_name, new_name)
    new_tree = renamer.visit(tree)
    return astor.to_source(new_tree)


# Example usage
if __name__ == "__main__":
    code = """
def example_function(old_param):
    print(old_param)
    old_param = old_param + 1
    return old_param
    """
    old_name = "old_param"
    new_name = "new_param"
    new_code = rename_parameter(code, old_name, new_name)
    print(new_code)