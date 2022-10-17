#!/usr/bin/python3
"""
a module containing simple class Rectangle
that defines a rectangle

"""


class Rectangle:
    """
    a simple class that defines a rectangle

    """
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle with width
        and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """

        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """

        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ computes the area of the given rectangle """

        return self.width * self.height

    def perimeter(self):
        """ calculates the perimeter of the given rectangle """

        if self.width == 0 or self.height == 0:
            return 0
        return self.width + self.height
