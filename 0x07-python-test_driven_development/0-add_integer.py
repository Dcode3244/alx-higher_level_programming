#!/usr/bin/python3
"""
my addition module
computes the addition of two given arguments

"""


def add_integer(a, b=98):
    """ returns a + b
    Args:
        a (int, float): first number to be added
        b (int, float): second number to be added
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
