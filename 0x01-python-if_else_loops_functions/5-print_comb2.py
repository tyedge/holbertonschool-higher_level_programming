#!/usr/bin/python3
for i in range(0, 100):
        if i == 99:
                print("{:s}".format(str(i)))
        else:
                print("{:>02s}".format(str(i)), end=', ')
