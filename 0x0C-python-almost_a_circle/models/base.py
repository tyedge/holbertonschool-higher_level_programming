#!/usr/bin/python3

""" This module defines the Base class and its attributes """

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
