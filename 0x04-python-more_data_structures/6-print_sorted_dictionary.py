#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary.items())
    for i in range(len(dict)):
        print('{}'.format(dict[i][0]) + ': ' + '{}'.format(dict[i][1]),
              end="\n")
