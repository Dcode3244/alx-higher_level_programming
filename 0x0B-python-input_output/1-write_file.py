#!/usr/bin/python3
""" defines a function that writes a string to a text file """


def write_file(file_name="", text=""):
    """ writes a string to a text file (UTF-8) and returns
    the number of character written """
    with open(file_name, 'w', encoding="utf-8") as fp:
        return fp.write(text)
