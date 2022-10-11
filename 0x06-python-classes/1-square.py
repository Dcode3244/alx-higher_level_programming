#!/usr/bin/python3
""" defines a square by:
Private instance attribute: size"""


class Square:
    """ a Square class """

    def __init__(self, size):
        """ Initializes a square
        Args:
            size (int): size of a square
        """
        self.__size = size
