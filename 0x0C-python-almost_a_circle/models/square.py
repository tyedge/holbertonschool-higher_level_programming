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

    @property
    def size(self):
        """ This getter function returns the size of a Square instance """
        return self.width

    @size.setter
    def size(self, size):
        """ This setter function validates and sets the size of a Square\
        instance """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ This function updates a Square instance """
        flist = ['id', 'size', 'x', 'y']
        fieldlist = [0, 0, 0, 0]
        idx = 0
        for arg in args:
            fieldlist[idx] = arg
            idx += 1
        if fieldlist[0] > 0:
            self.id = fieldlist[0]
        if fieldlist[1] > 0:
            self.width = fieldlist[1]
            self.height = fieldlist[1]
        if fieldlist[2] > 0:
            self.x = fieldlist[2]
        if fieldlist[3] > 0:
            self.y = fieldlist[3]
        if not args:
            for key, value in kwargs.items():
                if key in flist:
                    setattr(self, key, value)

    def to_dictionary(self):
        """This function returns a dictionary representation of a Rectangle"""
        new_dict = {'id': self.id, 'size': self.width, 'x': self.x, 'y':
                    self.y}
        return new_dict
