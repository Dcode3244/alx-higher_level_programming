#!/usr/bin/python3
""" defines a square by:
Private instance attribute: size"""


class Square:
    """ a Square class """

    def __init__(self, size=0):
        """ Initializes a square
        Args:
            size (int): size of a square
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ computes area of a square

        Returns:
            Area of a square
        """
        return (self.__size) ** 2
