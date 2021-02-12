"""Problem 32: Pandigital products

We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly
once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity,
39 × 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose
multiplicand/multiplier/product identity can be
written as a 1 through 9 pandigital. HINT: Some
products can be obtained in more than one way
so be sure to only include it once in your sum.
"""

from problem_24 import permutations


perms = permutations('123456789')

prods = []
for perm in perms:
    for i in range(1, len(perm)):
        mcand = int(perm[:i])
        rest = perm[i:]
        for j in range(1, len(rest)):
            mplier = int(rest[:j])
            prod = int(rest[j:])

            if mcand * mplier == prod:
                prods.append(prod)

print(sum(list(set(prods))))
