#!/usr/bin/python3
""" This function returns a peak number from an array, which is defined as a
number that is greater than its neighbors"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    arrlen = len(list_of_integers)
    start = 0
    end = arrlen - 1
    return peak_finder(list_of_integers, start, end, arrlen)


def peak_finder(arr, start, end, arrlen):
    """ This function finds the peak and returns to calling function """
    mid = int(start + (end - start) / 2)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == end or
                                                    arr[mid + 1] <= arr[mid])):
        return arr[mid]

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return peak_finder(arr, start, mid - 1, arrlen)

    else:
        return peak_finder(arr, mid + 1, end, arrlen)
