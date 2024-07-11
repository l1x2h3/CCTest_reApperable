import ast
import astor
import random
import string

class LocalVariableRenamer(ast.NodeTransformer):
    def __init__(self):
        self.local_vars = set()
        self.renamed_vars = {}

    def visit_FunctionDef(self, node):
        # Collect local variables in the function
        self.local_vars.clear()
        self.renamed_vars.clear()
        self._collect_local_vars(node)

        # Randomly select a local variable to rename
        if self.local_vars:
            var_to_rename = random.choice(list(self.local_vars))
            new_name = self._generate_new_name()
            self.renamed_vars[var_to_rename] = new_name

        # Continue visiting child nodes
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        # Rename occurrences of the local variable within the function body
        if isinstance(node.ctx, ast.Store) or isinstance(node.ctx, ast.Load):
            if node.id in self.renamed_vars:
                node.id = self.renamed_vars[node.id]
        return node

    def _collect_local_vars(self, node):
        for body_node in node.body:
            if isinstance(body_node, ast.Assign):
                for target in body_node.targets:
                    if isinstance(target, ast.Name):
                        self.local_vars.add(target.id)
            elif isinstance(body_node, ast.FunctionDef):
                self._collect_local_vars(body_node)

    def _generate_new_name(self):
        while True:
            new_name = ''.join(random.choices(string.ascii_lowercase, k=8))
            if new_name not in self.local_vars and new_name not in self.renamed_vars:
                return new_name

def rename_local_variable(code):
    tree = ast.parse(code)
    renamer = LocalVariableRenamer()
    new_tree = renamer.visit(tree)
    return astor.to_source(new_tree)

# Example usage
if __name__ == "__main__":
    code = """
def example_function():
    local_var = 10
    print(local_var)
    local_var = local_var + 1
    return local_var
    """
    new_code = rename_local_variable(code)
    print(new_code)