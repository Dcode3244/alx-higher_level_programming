#!/usr/bin/python3
"""
a module containing simple class Rectangle
that defines a rectangle

"""


class Rectangle:
    """
    a simple class that defines a rectangle

    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        print_symbol = Rectangle.print_symbol

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
        return (2 * (self.width + self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ print representation of the class Rectangle """

        if self.height > 0 and self.width > 0:
            for h in range(self.height):
                for w in range(self.width):
                    print(self.print_symbol, end="")
                if h < self.height - 1:
                    print("")
        return ("")

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
