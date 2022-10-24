#!/usr/bin/python3
"""  defines a function tha adds new atribute
    to an object if possible """


def add_attribute(obj, attr, val):
    """ adds a new attribute to an object if possible

    Args:
        obj (object): the object
        attr (str): the attribute to be added to the object
        val (str): value of the attribute
    """
    try:
        setattr(obj, attr, val)
    except Exception:
        raise TypeError("can't add new attribute")
