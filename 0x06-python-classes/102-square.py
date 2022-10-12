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

    @property
    def size(self):
        """ size getter

        Returns:
            size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size of a square

        Args:
            value (int): size of the new square
        """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ computes area of a square

        Returns:
            Area of a square
        """
        return (self.__size) ** 2

    def __lt__(self, other):
        """ checks if area 1 is less than area 2 """
        return (self.area() < other.area())

    def __le__(self, other):
        """ checks if area 1 is less than or equal to area 2 """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """ checks if area 1 is greater than area 2 """
        return (self.area() > other.area())

    def __ge__(self, other):
        """ checks if area 1 is greater than or equal to area 2 """
        return self.area() >= other.area()

    def __eq__(self, other):
        """ checks if two areas are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """ checks if two areas are not equal"""
        return self.area() != other.area()
