#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newrow = []
    newcol = []

    for i in matrix:
        for j in i:
            newcol.append(j ** 2)
        newrow.append(newcol)
        newcol = []
    return newrow
