Optimizer README
This project implements several optimization techniques aimed at improving the efficiency and performance of code. 
The optimizer processes input code files and applies the following techniques:

Constant Folding
Dead Code Elimination
Common Subexpression Elimination
Loop Unrolling

1. Constant Folding
Example:

Replaced 5 + 3 == 8 with 8 == 8
Replaced 0 == 1 with 0 == 1 (no change, but redundant evaluation removed)

2. Dead Code Elimination
Example:

Removed dead code IF 0 == 1
Removed code IF 1 == 0 as it’s never true

3. Common Subexpression Elimination
Example:

Reused a * b as x in multiple places to avoid recalculating the same value.

4. Loop Unrolling
Example:

Unrolled loop iteration 0, 1, and 2 to remove the loop control.

Example Output of Optimizations
Running optimizer on optimizer1.txt
Optimizations Applied:

Constant Folding: Replaced 5 + 3 == 8 with 8 == 8
Dead Code Elimination: Removed dead code IF 0 == 1
Common Subexpression Elimination: Reused a * b as x
Loop Unrolling: Unrolled loop iterations 0, 1, and 2
Optimized Code:

DO Task1
IF 8 == 8
    COMPLETE
DO Task2
    COMPLETE
DO Task3
x = a * b
y = x
DO Task4
i = 0
x = x + 1
i = 1
x = x + 1
i = 2
x = x + 1
    x = x + 1
COMPLETE

How to Use the Optimizer
Run the optimizer on each input file:
For example:
./optimizer.sh optimizer1.txt

