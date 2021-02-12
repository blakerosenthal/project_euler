"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

# This feels a bit messy. Takes over a minute on my laptop.

i = 1
divs = list(range(1,21))
while True:
    if all(i % d == 0 for d in divs):
        print(i)
        break
    
    i += 1
