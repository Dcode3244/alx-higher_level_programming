#!/usr/bin/python3
"""
    a module containing a class that inherits from list
"""


class MyList(list):
    """ a class that inherits from list """
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
