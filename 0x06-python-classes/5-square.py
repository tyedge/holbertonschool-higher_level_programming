#!/usr/bin/python3


class Square:
    """This is class defines a square """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.size == 0:
            print("")
        i = 0
        while i in range(self.size):
            print("{}".format("#" * self.size))
            i += 1
