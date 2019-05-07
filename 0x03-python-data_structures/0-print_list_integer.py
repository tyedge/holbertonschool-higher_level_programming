#!/usr/bin/python3

def print_list_integer(my_list=[]):
    x = 0
    while x < len(my_list):
        print(ord(chr(my_list[x]).format()))
        x += 1
