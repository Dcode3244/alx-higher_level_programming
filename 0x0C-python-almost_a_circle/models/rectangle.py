#!/usr/bin/python3
""" defines a rectangle class """
from models.base import Base


class Rectangle(Base):
    """ a class defining a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiates Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the
        character # """
        for y in range(self.__y):
            print()

        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ updates the class Rectangle attributes """
        attrs = ["id", "width", "height", "x", "y"]

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)

    def to_dictionary(self):
        """ returns dictionary representation of rectangle """
        return {
                'x': self.x,
                'y': self.y,
                'width': self.width,
                'height': self.height,
                'id': self.id
            }

    def __str__(self):
        """ returns description for the rectangle in the format-
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        ret1 = "[{}] ({})".format(self.__class__.__name__, self.id)
        ret2 = " {}/{}".format(self.__x, self.__y)
        ret3 = " - {}/{}".format(self.__width, self.__height)
        return ret1 + ret2 + ret3
