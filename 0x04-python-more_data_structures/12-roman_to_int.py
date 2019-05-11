#!/usr/bin/python3


def roman_to_int(roman_string):
    dict = {'I': "1", 'V': "5", 'X': "10", 'L': "50", 'C': "100", 'D': "500",
            'M': "1000"}
    sum = 0

    if not roman_string:
        return None
    if type(roman_string) != str:
        return 0
    if type(roman_string) != str:
        return 0

    for i in roman_string:
        if i in dict:
            sum += int(dict[i])
    if "IV" in roman_string or "IX" in roman_string:
        sum -= 2
    if "XL" in roman_string or "XC" in roman_string:
        sum -= 20
    if "CD" in roman_string or "CM" in roman_string:
        sum -= 200

    return sum
