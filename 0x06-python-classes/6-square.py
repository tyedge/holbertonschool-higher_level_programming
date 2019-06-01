#!/usr/bin/python3

msg = "position must be a tuple of 2 positive integers"


class Square:
    """This is class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        if type(position) is not tuple:
            raise TypeError(msg)
        if len(position) != 2:
            raise TypeError(msg)
        if type(position) is not int:
            raise TypeError(msg)
        if type(position) is not int:
            raise TypeError(msg)
        self.position = position

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

    @property
    def position(self):
        return self.__position

    def position(self, value):
        if type(value) is not tuple:
            raise TypeError(msg)
        if len(value) != 2:
            raise TypeError(msg)
        if type(value[0]) is not int:
            raise TypeError(msg)
        if type(value[1]) is not int:
            raise TypeError(msg)
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print("")
        if self.position[1] > 0:
            x = 0
            while x in range(self.position[1]):
                print('')
                x += 1
        i = 0
        while i in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
            i += 1
