import sys
import json

# Grammar rules
grammar = {
    'DO': ['TASK_NAME', 'IF_STATEMENT', 'COMPLETE'],
    'TASK_NAME': ['Task1', 'Task2', 'Task3'],
    'IF_STATEMENT': ['IF', 'IDENTIFIER', 'COMPARATOR', 'IDENTIFIER'],
    'IF': ['IF'],
    'COMPLETE': ['COMPLETE'],
    'IDENTIFIER': ['a', 'b', 'c', 'd', 'x', 'y', 'p', 'q'],
    'COMPARATOR': ['<', '>', '==', '!='],
}

def parse(tokens):
    ast = []
    while tokens:
        current_token = tokens.pop(0).strip()
        token_type, token_value = current_token.split(": ")
        if token_type == "DO":
            task_node = parse_task(tokens)
            if task_node:
                ast.append({"DO": task_node})
            else:
                raise SyntaxError("Invalid syntax after DO statement")
        else:
            raise SyntaxError(f"Unexpected token: {current_token}")
    return ast

def parse_task(tokens):
    task = {}

    # Parse TASK_NAME
    current_token = tokens.pop(0).strip() if tokens else None
    if current_token:
        token_type, token_value = current_token.split(": ")
        if token_type == "TASK_NAME" and token_value in grammar['TASK_NAME']:
            task['task_name'] = token_value
        else:
            raise SyntaxError(f"Invalid TASK_NAME: {token_value}")
    else:
        raise SyntaxError("Expected TASK_NAME after DO")

    # Parse IF_STATEMENT
    if tokens and tokens[0].startswith("IF:"):
        task['if_statement'] = parse_if_statement(tokens)
    else:
        raise SyntaxError("Expected IF statement after TASK_NAME")

    # Parse COMPLETE
    current_token = tokens.pop(0).strip() if tokens else None
    if current_token and current_token == "COMPLETE: COMPLETE":
        return task
    else:
        raise SyntaxError("Expected COMPLETE at the end of the statement")

def parse_if_statement(tokens):
    statement = {}

    # Process IF token
    current_token = tokens.pop(0).strip()
    token_type, token_value = current_token.split(": ")
    if token_type == "IF" and token_value == "IF":
        statement['if'] = token_value
    else:
        raise SyntaxError("Expected IF in IF_STATEMENT")

    # Process first IDENTIFIER
    current_token = tokens.pop(0).strip() if tokens else None
    if current_token:
        token_type, token_value = current_token.split(": ")
        if token_type == "IDENTIFIER" and token_value in grammar['IDENTIFIER']:
            statement['identifier1'] = token_value
        else:
            raise SyntaxError(f"Invalid IDENTIFIER: {token_value}")
    else:
        raise SyntaxError("Expected first IDENTIFIER in IF_STATEMENT")

    # Process COMPARATOR
    current_token = tokens.pop(0).strip() if tokens else None
    if current_token:
        token_type, token_value = current_token.split(": ")
        if token_type == "COMPARATOR" and token_value in grammar['COMPARATOR']:
            statement['comparator'] = token_value
        else:
            raise SyntaxError(f"Invalid COMPARATOR: {token_value}")
    else:
        raise SyntaxError("Expected COMPARATOR in IF_STATEMENT")

    # Process second IDENTIFIER
    current_token = tokens.pop(0).strip() if tokens else None
    if current_token:
        token_type, token_value = current_token.split(": ")
        if token_type == "IDENTIFIER" and token_value in grammar['IDENTIFIER']:
            statement['identifier2'] = token_value
        else:
            raise SyntaxError(f"Invalid IDENTIFIER: {token_value}")
    else:
        raise SyntaxError("Expected second IDENTIFIER in IF_STATEMENT")

    return statement

# Function to print the AST in the specified JSON format
def print_ast(ast):
    print(json.dumps(ast, indent=4))

# Main function to read input and start parsing
def main():
    # Read all tokens from the file
    with open("tokens.txt", "r") as file:
        tokens = file.read().strip().split("\n")

    try:
        # Parse the tokens and generate the AST
        ast = parse(tokens)

        # Print out the generated AST
        print("Generated AST:")
        print_ast(ast)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")

if __name__ == "__main__":
    main()
