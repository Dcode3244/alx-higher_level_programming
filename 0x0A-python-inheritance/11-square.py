#!/usr/bin/python3
""" defines a square class that inherits from BaseGeometry """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ a square class that inherits from BaseGeometry class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                        self.__size, self.__size))
