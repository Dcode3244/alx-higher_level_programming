#!/usr/bin/python3
""" defines a function that inserts a line of text to
a file, after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts  a line of text to a file after each line
    containing a specific string"""
    new = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            new += line
            if search_string in line:
                new += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new)
