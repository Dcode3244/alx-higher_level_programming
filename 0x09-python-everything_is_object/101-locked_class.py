#!/usr/bin/python3
"""
Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is
called first_name.
"""


class LockedClass:
    """
    a simple class that doesn't accept any attribute
    other the "first_name"
    """
    __slots__ = ['first_name']
