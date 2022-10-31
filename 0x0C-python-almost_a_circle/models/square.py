#!/usr/bin/python3
""" defines a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ updates attributes """
        attrs = ["id", "size", "x", "y"]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for idx, arg in enumerate(args):
                setattr(self, attrs[idx], arg)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """ print representation of the square instance """
        ret1 = "[{}] ({})".format(self.__class__.__name__, self.id)
        ret2 = " {}/{}".format(self.x, self.y)
        ret3 = " - {}".format(self.width)
        return ret1 + ret2 + ret3
