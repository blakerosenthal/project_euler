"""Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right
in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on
the diagonals is 101.

What is the sum of the numbers on the diagonals in
a 1001 by 1001 spiral formed in the same way?
"""

# sum of corners of n x n box
def corners(n):
    if n == 1:
        return 1
    
    c1 = n*n
    c2 = c1 - n+1
    c3 = c1 - 2*n+2
    c4 = c1 - 3*n+3
    
    return c1 + c2 + c3 + c4

c = 0
for i in range(1,1002,2):
    c += corners(i)

print(c)
