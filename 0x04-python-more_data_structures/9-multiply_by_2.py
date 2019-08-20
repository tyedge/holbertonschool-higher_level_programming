#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    mydict = a_dictionary.copy()
    for key in mydict:
        mydict[key] = mydict[key] * 2
    return mydict
