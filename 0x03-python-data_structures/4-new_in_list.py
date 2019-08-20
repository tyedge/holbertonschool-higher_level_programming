#!/usr/bin/python3


def new_in_list(my_list, idx, element):
        if not my_list:
                return None
        elif idx < 0:
                old = my_list
                return old
        elif idx > (len(my_list) - 1):
                old = my_list
                return old
        else:
                new = my_list.copy()
                new[idx] = element
                return new
