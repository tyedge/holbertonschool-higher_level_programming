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
        self.__width = width
        self.__height = height
