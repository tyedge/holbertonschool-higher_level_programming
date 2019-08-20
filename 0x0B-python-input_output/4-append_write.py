#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        var = f.write(text)
#        print(var, end='')
        return var
