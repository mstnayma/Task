VIDEO: https://youtu.be/fvUmyJuFU3I
Code Generation: This project implements a code generation phase for a custom programming language
 It processes an Abstract Syntax Tree (AST) generated from a custom source language, and converts it into a lower-level representation (assembly-like code).

Project Structure
scanner.py: Tokenizes the input source code into tokens.
parser.py: Parses the tokens into an Abstract Syntax Tree (AST).
code_generator.py: Generates a lower-level language (assembly-like) code from the AST.

How It Works
Tokenization (scanner.py):

The scanner.py script reads an input program (e.g., input2.txt) and tokenizes it into a sequence of tokens. These tokens are then saved to a file (tokens.txt).
Example Input:

'DO Task1 IF a < b COMPLETE\nDO Task1\nIF a < b\nCOMPLETE\nDO Task2\nIF c > d\nCOMPLETE'
Output: tokens.txt
Parsing (parser.py):

The parser.py script takes the tokenized file (tokens.txt) and generates an Abstract Syntax Tree (AST), which represents the hierarchical structure of the program.
Output: ast.json (contains the parsed structure of the program).
Code Generation (code_generator.py):

The code_generator.py script generates a lower-level code (similar to assembly code) based on the AST. The code is designed to execute specific operations based on the input program.
Example Output for input1.txt:
Task1:
LOAD a
LOAD b
COMPARE a, b
JUMP_IF_EQUAL IF  ; Jump if condition is met


Usage: 
Run the Scanner: Tokenize the input source code into tokens.
python3 scanner.py <input_file>

Run the Parser: Parse the tokens into an AST.
python3 parser.py <tokens_file>

Run the Code Generator: Generate the lower-level code from the AST.
python3 code_generator.py <input_file>

Example
Run the following commands:
Tokenize the input program:

python3 scanner.py input2.txt
Parse the tokens into an AST:
python3 parser.py tokens.txt
Generate the code from the AST:


python3 code_generator.py input2.txt
Example Output:
For input2.txt, the generated code might look like:
Task1:
LOAD a
LOAD b
COMPARE a, b
JUMP_IF_LESS_THAN IF  ; Jump if condition is met

Task2:
LOAD c
LOAD d
COMPARE c, d
JUMP_IF_GREATER_THAN IF  ; Jump if condition is met
Error Handling
The system is designed to log errors properly, indicating which stage (tokenization, parsing, or code generation) encountered the issue. For example, if there are syntax or semantic errors, these will be logged with specific error messages.

Example Error:
If there is an error in the input source code, the system will output an error like:

Syntax Error in parser: Unexpected token 'IF'
Sample Programs for Testing

Program 1:
DO Task1 IF a < b COMPLETE
DO Task1 IF a < b COMPLETE
Expected token output:
[ 'DO', 'Task1', 'IF', 'a', '<', 'b', 'COMPLETE' ]

Program 2 (simplified expressions):
DO Task1 IF a == b COMPLETE
Expected token output:
[ 'DO', 'Task1', 'IF', 'a', '==', 'b', 'COMPLETE' ]

Program 3 (with redundant code):
DO Task1 IF a == b COMPLETE
DO Task1 IF a == b COMPLETE
Expected token output:

[ 'DO', 'Task1', 'IF', 'a', '==', 'b', 'COMPLETE' ]

Program 4 (error handling):
DO Task1 IF a < b COMPLETES
Expected error output:

Syntax Error in scanner: Unexpected token 'COMPLETES'

Program 5 (semantic error):
DO Task1 IF a > b COMPLETE
Expected token output:
[ 'DO', 'Task1', 'IF', 'a', '>', 'b', 'COMPLETE' ]