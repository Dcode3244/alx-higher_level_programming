#!/usr/bin/python3
""" defines a function that reads a text file """


def read_file(filename=""):
    """ reads a file to stdout """

    with open(filename, encoding="utf-8") as fp:
        text = fp.read()

    print(text, end="")
