#!/bin/bash

# Run the scanner
python3 scanner.py "$1" > tokens.txt

# Run the parser
python3 parser.py tokens.txt
