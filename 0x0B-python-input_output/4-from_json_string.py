#!/usr/bin/python3
""" defines a function that returns and object represented
    by a JSON string """
import json


def from_json_string(my_str):
    """ returns object represented by a JSON string

    Args:
        my_str (str): the string
    Return:
        object represented by a JSON string
    """

    return (json.loads(my_str))
