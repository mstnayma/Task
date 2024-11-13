import sys

# Grammar rules (can be expanded as needed)
grammar = {
    'DO': ['TASK_NAME', 'IF_STATEMENT', 'COMPLETE'],
    'TASK_NAME': ['Task1', 'Task2'],
    'IF_STATEMENT': ['IF', 'IDENTIFIER', 'COMPARATOR', 'IDENTIFIER'],
    'IF': ['IF'],
    'COMPLETE': ['COMPLETE'],
    'IDENTIFIER': ['a', 'b', 'c', 'd'],
    'COMPARATOR': ['<', '>'],
}

# Function to parse tokens from stdin
def parse(tokens):
    ast = []
    while tokens:
        current_token = tokens.pop(0).strip()
        if current_token.startswith("DO"):
            ast.append({"DO": parse_task(tokens)})
    return ast

def parse_task(tokens):
    task = {}
    current_token = tokens.pop(0).strip()
    if current_token.startswith("TASK_NAME"):
        task['task_name'] = current_token.split(":")[1].strip()
    
    # Parse the IF statement
    task['if_statement'] = parse_if_statement(tokens)
    
    return task

def parse_if_statement(tokens):
    statement = {}
    
    # Process IF token
    current_token = tokens.pop(0).strip()
    if current_token.startswith("IF"):
        statement['if'] = current_token.split(":")[1].strip()
    
    # Process IDENTIFIER token (first one)
    current_token = tokens.pop(0).strip()
    if current_token.startswith("IDENTIFIER"):
        statement['identifier1'] = current_token.split(":")[1].strip()

    # Process COMPARATOR token
    current_token = tokens.pop(0).strip()
    if current_token.startswith("COMPARATOR"):
        statement['comparator'] = current_token.split(":")[1].strip()

    # Process IDENTIFIER token (second one)
    current_token = tokens.pop(0).strip()
    if current_token.startswith("IDENTIFIER"):
        statement['identifier2'] = current_token.split(":")[1].strip()

    return statement

# Main function to read input and start parsing
def main():
    # Read all tokens from stdin
    tokens = sys.stdin.read().strip().split("\n")

    # Now parse the tokens
    ast = parse(tokens)

    # Print out the generated AST
    print("Generated AST:")
    for item in ast:
        print(item)

if __name__ == "__main__":
    main()
