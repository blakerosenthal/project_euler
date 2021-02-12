"""
Some helper functions I use in multiple problems
"""

def factor(a: int) -> int:
    for i in range(2, a):
        if a % i == 0:
            return i, factor(int(a/i))
    
    return a

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def divisors(n: int) -> list:
    if n == 1:
        return [1]

    divisors = []
    i = 1
    j = n
    while i < j:
        if n % i == 0:
            j = int(n/i)
            divisors.append(i)

            if j != i:
                divisors.append(j)

        i += 1

    return divisors
