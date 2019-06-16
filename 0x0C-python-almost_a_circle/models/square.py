#!/usr/bin/python3

""" This module defines the Square Class and its attributes """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ This function initializes new instances of the Square Class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This function prints a special string for Square instances """
        return "[Square] (%s) %s/%s - %s" % (self.id, self.x, self.y,
                                             self.width)
