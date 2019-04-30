"""Finds the ASCII value of c and check for a lowercase letter"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
