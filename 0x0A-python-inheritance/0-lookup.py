#!/usr/bin/python3
"""
    module that return the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """ returls a list of available attributes and methods of an object """
    return dir(obj)
