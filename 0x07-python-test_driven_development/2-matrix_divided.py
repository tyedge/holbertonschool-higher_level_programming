#!/usr/bin/python3


def matrix_divided(matrix, div):
        newlist = []
        newmat = []
        if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("division by zero")
        for list in matrix:
                if len(matrix[0]) != len(list):
                        raise TypeError
                        ("Each row of the matrix must have the same size")
                for i in list:
                        if type(i) is not int and type(i) is not float:
                                raise TypeError("matrix must be a matrix (list\
                                of lists) of integers/floats")
                        x = round((i / div), 2)
                        newlist.append(x)
                newmat.append(newlist)
                newlist = []
        return newmat
