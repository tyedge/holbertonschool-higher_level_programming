#!/usr/bin/python3

val = False
truthy = []


def divisible_by_2(my_list=[]):
    global truthy, val
    if not my_list:
        return None
    for i in my_list:
        if i is 0:
            val = True
        elif i % 2 is 0:
            val = True
        else:
            val = False
        truthy.append(val)
    return truthy
