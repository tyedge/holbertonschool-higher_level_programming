#!/usr/bin/python3


def no_c(my_string):
        if not my_string:
                return None
        translation = {99: None, 67: None}
        return my_string.translate(translation)
