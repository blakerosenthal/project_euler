"""Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations
of 0, 1 and 2 are:

012 021 102 120 201 210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permutations(digits: str) -> list:
    """returns list of every permutation
    of characters in 'digits'
    """
    if len(digits) == 1:
        return [digits]

    if len(digits) == 2:
        return [digits, digits[::-1]]

    ret = []
    for digit in digits:
        i = digits.index(digit)
        copy = digits[:i] + digits[i+1:]
        for perm in permutations(copy):
            ret.append(f'{digit}{perm}')
    
    return ret


if __name__ == '__main__':

    # this unnecessarily calculates every permutation
    # (there are 3628800), instead of just the first
    # million. it's plenty fast though.
    perms = sorted(permutations('0123456789'))
    print(perms[999_999])
