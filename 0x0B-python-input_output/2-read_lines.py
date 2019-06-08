#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    lines = 0
    with open(filename, 'r', encoding='utf-8') as filer:
        for line in filer:
            lines += 1
            if nb_lines > 0 and nb_lines <= lines:
                print(line)
        print(filer.read())
