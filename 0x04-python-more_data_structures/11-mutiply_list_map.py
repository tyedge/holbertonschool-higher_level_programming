#!/usr/bin/python3


def mutiply_list_map(my_list=[], number=0):
    if not my_list:
        return None
    return(list(map(lambda n: n * number, my_list)))
