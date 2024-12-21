#!/bin/bash
for i in input1.txt input2.txt input3.txt input4.txt input5.txt input6.txt input7.txt
do
    python3 scanner.py $i
    python3 parser.py tokens.txt
done

# Loop through each optimizer file and run the optimizer
for i in optimizer1.txt optimizer2.txt optimizer3.txt optimizer4.txt optimizer5.txt
do
    echo "Running optimizer on $i"
    python3 optimizer.py $i
done