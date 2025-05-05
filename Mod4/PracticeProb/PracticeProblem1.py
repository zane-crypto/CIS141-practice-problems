'''
Construct a truth table for the expression:
(A AND B) OR (NOT B) where A and B each can
be True or False. Your truth table should be
commented out (as it's not valid Python code!)
'''
'''
#1. List variables
    A, B

#2. Deterimine the number of rows
    2 combinations for A
    2 combinations for B
    2x2 combinations of A&B
    
#3. Create table columns
    A   B   (A AND B)   (NOT B) (A AND B) OR (NOT B)
 
#4. Enumerate all possible (A, B) combinations
    A   B   (A AND B)   (NOT B) (A AND B) OR (NOT B)
    0   0
    0   1
    1   0
    1   1
    
#5. Fill each row with sub-expression results
     A   B   (A AND B)   (NOT B) (A AND B) OR (NOT B)
    0   0       0           1               1
    0   1       0           0               0
    1   0       0           1               1
    1   1       1           0               1
'''
