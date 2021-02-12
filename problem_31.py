"""Problem 31: Coin sums

In the United Kingdom the currency is made up of
pound (£) and pence (p). There are eight coins in
general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any
number of coins?
"""

COINS = [200, 100, 50, 20, 10, 5, 2, 1]
CACHE = {0: []}


def make_change(amnt):
    """returns list of tuples that represent unique
    ways to make change from 'amnt'
    
    >>> make_change(5)
    [(1, 2, 2), (5,), (1, 1, 1, 1, 1), (1, 1, 1, 2)]
    """
    if amnt in CACHE:
        return CACHE[amnt]

    ways = []
    possible_coins = [c for c in COINS if c <= amnt]
    
    for p in possible_coins:
        
        if amnt == p:
            ways.append((p,))

        for w in make_change(amnt-p):
            ways.append(w+(p,))
    
    ways = list({tuple(sorted(list(w))) for w in ways})
    CACHE[amnt] = ways
    
    return ways


print(len(make_change(200)))
