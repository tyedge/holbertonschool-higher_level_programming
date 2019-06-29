#!/usr/bin/python3

""" This module defines the Base class and its attributes """
import json
from os import path


class Base:
    """ This is the Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This function initializes new instances of this class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This function returns the JSON string representation of\
        list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ This function returns the list of the JSON string representation\
        json_string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This function writes the JSON string representation of list_objs\
        to a file """
        filename = cls.__name__ + '.json'
        dlist = []
        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                var = file.write(cls.to_json_string([]))
            else:
                for list in list_objs:
                    dict = list.to_dictionary()
                    dlist.append(dict)
                var = file.write(cls.to_json_string(dlist))
            return var

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            reckie = cls(1, 1)
            reckie.update(**dictionary)
            return reckie
        elif cls.__name__ == 'Square':
            sqr = cls(1)
            sqr.update(**dictionary)
            return sqr

    @classmethod
    def load_from_file(cls):
        """ This function returns a list of instances """
        oth = []
        lins = []
        filename = cls.__name__ + '.json'
        if not path.exists(filename):
            return "[]"
        else:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    var = cls.from_json_string(line)
                    for i in var:
                        lins.append(i)
            for t in lins:
                test = cls.create(**t)
                print(test)
                oth.append(test)
            return oth
