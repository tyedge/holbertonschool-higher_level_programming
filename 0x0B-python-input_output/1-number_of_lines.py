#!/usr/bin/python3
def number_of_lines(filename=""):
    linenum = 0
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            linenum += 1
    return linenum
