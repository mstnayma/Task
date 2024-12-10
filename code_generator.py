import json

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate_code(self):
        generated_code = []
        for do_statement in self.ast:
            if isinstance(do_statement, dict):  # Ensure it's a dictionary
                if "DO" in do_statement:
                    do_block = do_statement["DO"]
                    task_name = do_block["task_name"]
                    if_statement = do_block["if_statement"]
                    if_code = self.generate_if_statement(if_statement)
                    do_code = f"{task_name}:\n{if_code}"
                    generated_code.append(do_code)
                else:
                    print(f"Error: Missing 'DO' key in do_statement: {do_statement}")
            else:
                print(f"Error: do_statement is not a dictionary: {do_statement}")
        return "\n".join(generated_code)

    def generate_if_statement(self, if_statement):
        # Extract components of the if statement
        if_type = if_statement["if"]
        identifier1 = if_statement["identifier1"]
        comparator = if_statement["comparator"]
        identifier2 = if_statement["identifier2"]

        # Optimize for trivial conditions
        if identifier1 == identifier2 and comparator == "==":
            # For conditions like a == a, avoid redundant code
            return f"LOAD {identifier1}\nLOAD {identifier1}\nJUMP_IF_EQUAL {identifier1}, {identifier2}  ; Condition is always true, skipping comparison\n"
        
        if identifier1 == identifier2 and comparator == "!=":
            # For conditions like a != a, the condition is always false (skip code generation)
            return f"LOAD {identifier1}\nLOAD {identifier1}\nJUMP_IF_NOT_EQUAL {identifier1}, {identifier2}  ; Condition is always false, skipping comparison\n"

        # Now generate pseudo-assembly code for comparison
        if comparator == "==":
            compare_op = "COMPARE"
            jump_op = "JUMP_IF_EQUAL"
        elif comparator == "<":
            compare_op = "COMPARE"
            jump_op = "JUMP_IF_LESS_THAN"
        elif comparator == ">":
            compare_op = "COMPARE"
            jump_op = "JUMP_IF_GREATER_THAN"
        elif comparator == "!=":
            compare_op = "COMPARE"
            jump_op = "JUMP_IF_NOT_EQUAL"
        else:
            print(f"Error: Unsupported comparator {comparator}")
            return ""

        # Pseudo-assembly code for comparison
        code = f"LOAD {identifier1}\n"  # Load first identifier into register
        code += f"LOAD {identifier2}\n"  # Load second identifier into register
        code += f"{compare_op} {identifier1}, {identifier2}\n"  # Compare identifiers
        code += f"{jump_op} {if_statement['if']}  ; Jump if condition is met\n"  # Conditional jump

        return code

# Function to read AST from 'ast.json'
def load_ast_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    ast_data = load_ast_from_file('ast.json')  # Load AST from the JSON file

    # Iterate over the loaded AST data
    for ast in ast_data:
        code_generator = CodeGenerator([ast])  # Pass a list with the single ast item
        generated_code = code_generator.generate_code()
        print(generated_code)

if __name__ == "__main__":
    main()
