#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    val = a_dictionary.items()
    new = []

    for i in val:
        if i[1] == value:
            new.append(i[0])

    for j in new:
        del a_dictionary[j]

    return a_dictionary
