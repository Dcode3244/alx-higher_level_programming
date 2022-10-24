#!/usr/bin/python3
""" defines a object class checking function """


def is_same_class(obj, a_class):
    """ checks if an obj is exactly an instance of the specified class

    Args:
        obj (object): the object to be checked
        a_class ( class name): the class name
    Return:
        True if the object is exactly an instance of the specified class
    """
    return True if type(obj) == a_class else False
