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
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ postion getter """

        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def __str__(self):
        """ the print() representation of a Square class """
        val = []
        if self.__size == 0:
            return "\n"
        else:
            for i in range(self.__position[1]):
                val.append("\n")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    val.append(" ")
                for j in range(self.__size):
                    val.append("#")
                if i != self.size - 1:
                    val.append("\n")
        return ("".join(val))
