#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    elif idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list.remove(my_list[idx])
        return my_list
