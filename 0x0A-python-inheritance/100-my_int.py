#!/usr/bin/python3
""" defines Myint class that inherits from int """


class MyInt(int):
    """ a class that inherits from int """
    def __eq__(self, other):
        return self.numerator != other

    def __ne__(self, other):
        return self.numerator == other
