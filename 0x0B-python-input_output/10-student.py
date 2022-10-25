#!/usr/bin/python3
""" defines a class Student that defines a student """


class Student:
    """ a class that defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (not isinstance(attrs, list) or
                all(not isinstance(s, str) for s in attrs)):
            return self.__dict__
        new = dict()
        for attr in attrs:
            if attr in self.__dict__:
                new[attr] = (self.__dict__)[attr]
        return new
