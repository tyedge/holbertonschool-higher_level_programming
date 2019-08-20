#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    linenum = 1
    with open(filename, 'r', encoding='utf-8') as filer:
        while linenum <= nb_lines:
            var = filer.readline()
            print(var, end='')
            linenum += 1
        if nb_lines <= 0 or nb_lines > linenum:
            print(filer.read(), end='')
