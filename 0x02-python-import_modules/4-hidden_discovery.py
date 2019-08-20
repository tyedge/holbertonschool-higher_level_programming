#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    import hidden_4
    res = dir(hidden_4)
    for i in res:
        if i.startswith('__') is False:
            print(i)
