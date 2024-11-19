TaskFlow Parser

TaskFlow CFG: 
S -> DO TASK_NAME IF STATEMENT COMPLETE
TASK_NAME -> Task1 | Task2 | Task3 | Task4 |
STATEMENT -> IF IDENTIFIER COMPARATOR IDENTIFIER
IF -> "IF"
IDENTIFIER -> [a-zA-Z_][a-zA-Z0-9_]*
COMPARATOR -> "==" | "!=" | "<" | ">"
COMPLETE -> "COMPLETE"

Non-terminal symbols:

S (Start symbol)
TASK_NAME
STATEMENT
IF
IDENTIFIER

Terminal symbols: DO, TASK_NAME, IF, COMPLETE, IDENTIFIER, COMPARATOR

Parsing Algorithm: 
I have developed a recursive descent parser to parse the task descriptions and generate an Abstract Syntax Tree (AST). 
The parser processes the tokens produced by the scanner, checking for correctness according to the CFG defined above.

Key Features:

The parser handles syntax errors gracefully, providing meaningful error messages when the input doesn't match the expected structure.
If the input is syntactically correct, the parser outputs the corresponding AST.

Example AST for DO Task1 IF a == b COMPLETE:
{
  "type": "Task",
  "task_name": "Task1",
  "if_statement": {
    "type": "IfStatement",
    "left": "a",
    "comparator": "==",
    "right": "b"
  }
}




