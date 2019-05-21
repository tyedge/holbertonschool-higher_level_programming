#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    retval = []
    num = 0
    x = 0
    while x in range(list_length):
        try:
            num = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            retval.append(num)
        num = 0
        x += 1
    return retval
