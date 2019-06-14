#!/usr/bin/python3

""" This module defines the Rectangle Class and its attributes """
from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle Class. It is a subclass of the Base Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This function initializes new instances of the Rectangle Class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ This getter function returns the width of Rectangle instances """
        return self.__width

    @property
    def height(self):
        """ This getter function returns the height of Rectangle instances """
        return self.__height

    @property
    def x(self):
        """ This getter function returns the x value of Rectangle instances """
        return self.__x

    @property
    def y(self):
        """ This getter function returns the y value of Rectangle instances """
        return self.__y

    @width.setter
    def width(self, width):
        """ This setter function validates and sets the value of the width\
        variable of Rectangle instances """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ This setter function validates and sets the value of the height\
        variable of Rectangle instances """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ This setter function validates and sets the value of the x\
        variable of Rectangle instances """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ This setter function validates and sets the value of the y\
        variable of Rectangle instances """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ This function calculates and returns the area of a Rectangle\
        instance """
        return self.__width * self.__height

    def display(self):
        """ This function prints a Rectangle instance to stdout, using '#' """
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """ This function prints a special string for Rectangle instances """
        return "[Rectangle] (%s) %s/%s - %s/%s" % (self.id, self.__x, self.__y,
                                                   self.__width, self.__height)

    def update(self, *args, **kwargs):
        """This function updates some or all fields of a Rectangle instance"""
        fieldlist = [0, 0, 0, 0, 0]
        idx = 0
        while idx < (len(args)):
            for arg in args:
                fieldlist[idx] = arg
                idx += 1
        if fieldlist[0] > 0:
            self.id = fieldlist[0]
        if fieldlist[1] > 0:
            self.__width = fieldlist[1]
        if fieldlist[2] > 0:
            self.__height = fieldlist[2]
        if fieldlist[3] > 0:
            self.__x = fieldlist[3]
        if fieldlist[4] > 0:
            self.__y = fieldlist[4]
        else:
            if not args:
                for key, value in kwargs.items():
                    if key is "id":
                        self.id = value
                    if key is "width":
                        self.__width = value
                    if key is "height":
                        self.__height = value
                    if key is "x":
                        self.__x = value
                    if key is "y":
                        self.__y = value
