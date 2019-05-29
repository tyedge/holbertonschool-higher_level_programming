#!/usr/bin/python3


class Rectangle:
    """This class governs the attributes of retangles and squares

    The __init__ method initializaes each instantiation of the Rectangle
    class.

    Args:
        width (:obj: `int`, optional): optional parameter given by the caller
            which defines the width of of a rectangle instance
        height (:obj: `int`, optional): optional parameter given by the caller
            which defines the height of a rectangle instance

    Attributes:
        width (int): the width of of a rectangle instance
        height (int): the height of a rectangle instance
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        x = ''
        if self.__width != 0 and self.__height != 0:
            i = 1
            while i in range(self.__height):
                x += '%s\n' % ('#' * self.__width)
                i += 1
            x += '%s' % ('#' * self.__width)
        return x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
