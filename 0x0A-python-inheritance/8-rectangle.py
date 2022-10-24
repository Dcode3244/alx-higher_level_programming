#!/usr/bin/python3
""" defines a rectangle class that inherits from BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ a rectangle class that inherits from BaseGeometry class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height
