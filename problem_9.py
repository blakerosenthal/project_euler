"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural
numbers, a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet
for which a + b + c = 1000. Find the product abc.
"""

def bad_bad_bad():
    """This is probably the worst possible way to do this.
    Takes a solid ten seconds on my laptop.
    """
    for i in range(1, 1000 + 1):
        for j in range(1, 1000 + 1):
            for k in range(1, 1000 + 1):
                if i + j + k == 1000 and i**2 + j**2 == k**2:
                    return i, j, k

triplet = bad_bad_bad()
print('triplet:', triplet)
print('product:', triplet[0]*triplet[1]*triplet[2])
