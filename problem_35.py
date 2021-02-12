"""Problem 35: Circular primes

The number, 197, is called a circular prime
because all rotations of the digits: 197, 971,
and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3,
5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from helpers import is_prime


def rotations(digits: str) -> list:
    ret = []
    for i in range(len(digits)):
        first, last = digits[:i], digits[i:]
        ret.append(f'{last}{first}')
    
    return ret

circ_primes = []
for i in range(1_000_000):
    if i in circ_primes:
        next

    perms = list(map(int, rotations(str(i))))
    
    if all(is_prime(num) for num in perms):
        circ_primes += perms

print(len(sorted(list(set(circ_primes)))))
