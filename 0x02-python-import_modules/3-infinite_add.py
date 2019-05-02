#!/usr/bin/python3


def adder():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description='Add integers from the commandline')
        parser.add_argument('nums', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        parser.add_argument('--sum', dest='total', action='store_const',
                            const=sum, default=sum, help='sum function')
        args = parser.parse_args()
        print(args.total(args.nums))
    else:
        print(0)

if __name__ == "__main__":
    import sys
    import argparse
    adder()
