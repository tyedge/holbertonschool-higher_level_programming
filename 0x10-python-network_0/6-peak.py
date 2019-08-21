#!/usr/bin/python3
""" This function returns a peak number from an array, which is defined as a
number that is greater than its neighbors"""


def find_peak(arr=[]):
    if not arr:
        return
    arrlen = len(arr)
    if arrlen % 2 == 0:
        arrlen = arrlen - 1
    start = arr[0]
    end = arr[arrlen - 1]

    while start < end:
        mid = round((start + (end - start))/2)
        if arr[mid] < arr[mid + 1]:
            start = arr[mid + 1]
        else:
            end = arr[mid]

    return start
