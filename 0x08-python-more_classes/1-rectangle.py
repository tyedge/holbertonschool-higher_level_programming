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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        width = value
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        height = value
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
