#!/usr/bin/python3

import sys


def arg_info():
    count = len(sys.argv[1:])
    arg = str(count) + " argument"

    if count == 0:
        arg = arg + "s."
    elif count == 1:
        arg = arg + ":"
    else:
        arg = arg + "s:"
    print(arg)

    x = 0
    for i in sys.argv[1:]:
        x += 1
        print("{}: {}".format(x, i))

if __name__ == "__main__":
    arg_info()
