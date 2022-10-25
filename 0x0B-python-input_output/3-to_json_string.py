#!/usr/bin/python3
""" defines a function that returns the JSON representation
    of an object """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object

    Args:
        my_obj (object): the object
    Return:
        JSON representation on my_obj
    """

    return (json.dumps(my_obj))
