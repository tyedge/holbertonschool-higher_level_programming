#!/usr/bin/python3


class Student:
    """ The Student Class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = self.__dict__
        if attrs is None:
            return dict
        else:
            dict2 = {}
            for i in attrs:
                if type(i) is str:
                    for k, v in dict.items():
                        if i == k:
                            dict2[k] = v
            return dict2
