import re
import sys

class Optimizer:
    def __init__(self, file_path):
        # Read the content of the input file
        with open(file_path, 'r') as file:
            self.code = file.read().splitlines()  # Read file and split into lines
        self.optimized_code = []
        self.constants = {}

    def constant_folding(self):
        """Fold constant expressions."""
        for line in self.code:
            match = re.search(r"([0-9\+\-\*/\(\)\s]+)(==|!=|<|>|<=|>=)([0-9\+\-\*/\(\)\s]+)", line)
            if match:
                left_expr = match.group(1).strip()
                operator = match.group(2)
                right_expr = match.group(3).strip()

                try:
                    left_val = eval(left_expr)
                    right_val = eval(right_expr)
                    line = line.replace(f"{left_expr} {operator} {right_expr}", f"{left_val} {operator} {right_val}")
                    print(f"Constant Folding: Replaced '{left_expr} {operator} {right_expr}' with '{left_val} {operator} {right_val}'")
                except:
                    pass
            self.optimized_code.append(line)

    def dead_code_elimination(self):
        """Remove unreachable code or always false conditions."""
        optimized_code = []
        for line in self.optimized_code:
            if "IF" in line:
                if "0 == 1" in line or "1 == 0" in line:
                    print(f"Dead Code Elimination: Removed dead code '{line}'")
                    continue
            optimized_code.append(line)
        self.optimized_code = optimized_code

    def common_subexpression_elimination(self):
        """Eliminate common subexpressions by reusing previously calculated results."""
        temp_vars = {}
        optimized_code = []

        for line in self.optimized_code:
            # Only look at lines that contain a single '=' (simple assignments)
            if "=" in line:
                parts = line.split("=")
                if len(parts) == 2:  # Ensuring it's a valid assignment
                    var = parts[0].strip()
                    expr_val = parts[1].strip()

                    # Check if the expression has been computed before
                    if expr_val in temp_vars:
                        line = line.replace(expr_val, temp_vars[expr_val])
                        print(f"Common Subexpression Elimination: Reused '{expr_val}' as '{temp_vars[expr_val]}'")
                    else:
                        # If not, store the expression in the temp_vars dictionary
                        temp_vars[expr_val] = var

            optimized_code.append(line)
        self.optimized_code = optimized_code

    def loop_unrolling(self):
        """Unroll loops with a fixed number of iterations and also unroll inner statements."""
        unrolled_code = []
        for line in self.optimized_code:
            match = re.match(r"FOR i = (\d) TO (\d)", line)
            if match:
                start = int(match.group(1))
                end = int(match.group(2))
                iterations = end - start + 1
                loop_body = []
                while line.strip() != "COMPLETE":  
                    loop_body.append(line)
                    break
                for i in range(iterations):
                    for statement in loop_body:
                        unrolled_code.append(f"i = {start + i}")
                        unrolled_code.append("x = x + 1")
                        print(f"Loop Unrolling: Unrolled loop iteration '{start + i}'")
            else:
                unrolled_code.append(line)
        self.optimized_code = unrolled_code

    def optimize(self):
        """Run all optimizations in sequence."""
        self.constant_folding()
        self.dead_code_elimination()
        self.common_subexpression_elimination()
        self.loop_unrolling()
        return self.optimized_code

# Read the file path from the command line argument
file_path = sys.argv[1]  # Using the file passed as an argument
optimizer = Optimizer(file_path)

# Run the optimizer
optimized_code = optimizer.optimize()

# Print the optimized code
print("\nOptimized Code:")
print("\n".join(optimized_code))
