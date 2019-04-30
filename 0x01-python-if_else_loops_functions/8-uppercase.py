#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if i.isalpha() and (ord(i) >= 97 and ord(i) <= 122):
            i = ord(i) - 32
        else:
            i = ord(i)
        print("{:s}".format(chr(i)), end='')
    print()
