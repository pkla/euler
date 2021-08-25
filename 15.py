"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial

def multiset(n, k):
    res = factorial(n)
    for m in k:
        res /= factorial(m)
    return res

def lattice_path(n):
    return multiset(n*2, [n, n])

def euler_15():
    return lattice_path(20)

if __name__ == "__main__":
    print(euler_15())