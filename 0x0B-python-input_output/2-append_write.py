#!/usr/bin/python3
""" defines a function that appends a string to a text file """


def append_write(file_name="", text=""):
    """ appends a string to a text file (UTF-8) and returns
    the number of character written """
    with open(file_name, 'a', encoding="utf-8") as fp:
        return fp.write(text)
