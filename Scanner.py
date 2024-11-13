import re
import sys

class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code.strip()  # Strip any leading/trailing whitespace
        self.tokens = []

    def tokenize(self):
        # Define token patterns for different token types
        patterns = [
            (r"DO", "DO"),
            (r"Task[1-4]", "TASK_NAME"),  # Specific pattern for task
            (r"IF", "IF"),
            (r"COMPLETE", "COMPLETE"),
            (r"PENDING", "PENDING"),
            (r"<|>|==|!=", "COMPARATOR"),
            (r"[a-zA-Z_][a-zA-Z0-9_]*", "IDENTIFIER"),  # More general identifier pattern
            (r"\s+", None),  # Ignore whitespace
        ]

        position = 0
        while position < len(self.source_code):
            match = None
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(self.source_code, position)
                if match:
                    if token_type:  # Ignore whitespace
                        self.tokens.append((token_type, match.group(0)))
                    position = match.end()
                    break  # Exit the loop once a match is found
            if not match:
                raise SyntaxError(f"Unexpected character: {self.source_code[position]}")

    def get_tokens(self):
        # Return the list of tokens as strings in the form: 'TOKEN_TYPE: value'
        return [f"{token_type}: {value}" for token_type, value in self.tokens]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Open the input file, read its content, and close it
    try:
        with open(input_file, "r") as file:
            source_code = file.read().strip()  # Strip leading/trailing whitespace here as well
            print(repr(source_code))  # Debugging: Check the raw content of the file
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)

    scanner = Scanner(source_code)
    
    # Tokenize the input program
    scanner.tokenize()

    # Print the tokens directly to the terminal
    for token in scanner.get_tokens():
        print(token)

    print("Tokenization complete.")
