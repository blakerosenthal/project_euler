"""Problem 27: Quadratic primes
"""

from helpers import is_prime


def cons_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    
    return n

a = -999
b = -999
max_primes = 0

for i in range(-999, 1000):  # a
    for j in range(-999, 1000):
        p = cons_primes(i,j)
        if p > max_primes:
            a, b = i, j
            max_primes = p

print('a:', a)
print('b:', b)
print('max primes:', max_primes)
print('product (answer):', a * b)
