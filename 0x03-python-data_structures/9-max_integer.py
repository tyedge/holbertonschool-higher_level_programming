#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None
    retval = 0
    for i in my_list:
        if i > retval:
            retval = i
    return retval
