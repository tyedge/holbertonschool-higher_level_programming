#!/usr/bin/python3


class Student:
    """ The Student Class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        return self.__dict__
