"""
Problem 25: 1000-digit Fibonacci number

F_1 = 1 and F_2 = 1 The 12th term,
F_12 = 144, is the first term to contain
three digits.

What is the index of the first term in
the Fibonacci sequence to contain 1000 digits?
"""

a = 1
b = 1
idx = 2
while len(str(b)) != 1000:
    a, b = b, a+b
    idx += 1

print(idx)
