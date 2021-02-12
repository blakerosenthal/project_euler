"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import is_prime


tot = 0
for i in range(2_000_000):
    if is_prime(i):
        tot += i

print(tot)
