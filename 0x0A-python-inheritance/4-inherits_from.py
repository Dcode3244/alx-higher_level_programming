#!/usr/bin/python3
""" defines a object inheritance checking function """


def inherits_from(obj, a_class):
    """ checks if an obj is an instance of the class that unherited
        directly or indirectly from the specified class

    Args:
        obj (object): the object to be checked
        a_class ( class name): the class name
    Return:
        True if the object is instance of class that inherited
        from the specified class. Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
