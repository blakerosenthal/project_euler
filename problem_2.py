"""
Problem 2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the
even-valued terms.
"""

a = 0
b = 1
tot = 0
while b < 4_000_000:
    if b % 2 == 0:
        tot += b
    a, b = b, a + b

print(tot)