#!/usr/bin/python3
""" defines a square by:
Private instance attribute: size"""


class Square:
    """ a Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a square
        Args:
            size (int): size of a square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ postion getter """

        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """

        self.__position = value
        if (not isinstance(value, tuple) or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ computes area of a square

        Returns:
            Area of a square
        """
        return (self.__size) ** 2

    def my_print(self):
        """ prints a square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()