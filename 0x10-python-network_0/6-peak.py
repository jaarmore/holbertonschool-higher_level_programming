#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    high = len(list_of_integers) - 1
    low = 0
    lis = list_of_integers
    while high > low:
        mid = (high + low) // 2
        if lis[mid] <= lis[mid + 1]:
            low = mid + 1
        elif lis[mid] <= lis[mid - 1]:
            high = mid - 1
        elif lis[mid] >= lis[mid + 1] and lis[mid] >= lis[mid - 1]:
            return lis[mid]
    return lis[low]
