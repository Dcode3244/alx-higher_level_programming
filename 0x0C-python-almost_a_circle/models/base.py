#!/usr/bin/python3
""" defines a class Base """
import json
import csv
import turtle


class Base:
    """ a class that manages id attribute in all our classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiates the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        fname = cls.__name__ + ".json"

        with open(fname, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_list = []
                for obj in list_objs:
                    val = obj.to_dictionary()
                    dict_list.append(val)
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string
        representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if "size" in dictionary:
            dummy = cls(dictionary["size"])
        else:
            dummy = cls(dictionary["width"], dictionary["height"])

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            fname = cls.__name__ + ".json"
            with open(fname, "r", encoding="utf-8") as f:
                js = cls.from_json_string(f.read())
                instances = []
                for inst in js:
                    instances.append(cls.create(**inst))
            return instances

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves csv serialization of list_objs to file """
        fname = cls.__name__ + ".csv"

        with open(fname, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldNames = ["id", "width", "height", "x", "y"]
                else:
                    fieldNames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldNames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ returns list of classes deserialized from csv file """
        try:
            fname = cls.__name__ + ".csv"
            with open(fname, "r", encoding="utf-8") as f:
                if cls.__name__ == "Rectangle":
                    fieldNames = ["id", "width", "height", "x", "y"]
                else:
                    fieldNames = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(f, fieldnames=fieldNames)
                dict_list = [dict([key, int(val)] for key, val
                                  in d.items()) for d in dict_list]
                return [cls.create(**d) for d in dict_list]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b53e3a")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#d9d7d7")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#a5d1c7")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
