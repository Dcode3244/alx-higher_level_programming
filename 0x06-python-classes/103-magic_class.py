#!/usr/bin/python3

""" a MagicClass representing a circle """


import math


class MagicClass:
    """ a class representing a circle """

    def __init__(self, radius=0):
        """ initialize the MagicClass

        Arg:
            radius (int or float): radius of the circle
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """ computes area of a MagicClass circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Computes a circumference of a MagicClass circle """
        return 2 * math.pi * self.__radius
