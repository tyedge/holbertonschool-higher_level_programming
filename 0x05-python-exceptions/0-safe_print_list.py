#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    try:
        a = 0
        for i in my_list[:x]:
            print("{}".format(i), end='')
            a += 1
        print('')
        return a

        raise IndexError

    except IndexError:
        print("Oops! Index out of range")
