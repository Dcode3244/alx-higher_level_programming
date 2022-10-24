#!/usr/bin/python3
""" defines a square class that inherits from BaseGeometry """


BaseGeometry = __import__("9-rectangle").BaseGeometry


class Square(BaseGeometry):
    """ a square class that inherits from BaseGeometry class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
