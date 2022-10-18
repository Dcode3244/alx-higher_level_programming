#!/usr/bin/python3
"""
a simple module that prints a square with # character

"""


def print_square(size):
    """
    prints a square of given size with a
    # character

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
