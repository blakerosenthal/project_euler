"""
Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down, there are exactly
6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# These are the binomial coefficients (Pascal's Triangle).
# How many ways can you choose 20 segments from 40 options
# (20 to the right and 20 down)

from math import factorial
factorial(40) // (factorial(20) * factorial(40 - 20))
