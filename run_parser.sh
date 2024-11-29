#!/bin/bash
for i in input1.txt input2.txt input3.txt input4.txt input5.txt input6.txt input7.txt
do
    python3 scanner.py $i
    python3 parser.py tokens.txt
done
