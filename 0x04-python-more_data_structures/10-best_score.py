#!/usr/bin/python3

top = ""


def best_score(a_dictionary):
    global top
    if not a_dictionary:
        return None
    maxer = -2147483648
    for i in a_dictionary:
        if a_dictionary[i] > maxer:
            maxer = a_dictionary[i]
            top = i
    return top
