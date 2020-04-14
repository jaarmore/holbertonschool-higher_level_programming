#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    if list_of_integers:
        aux = list_of_integers
        start = 0
        end = len(list_of_integers) - 1
        mid = (start + end) // 2

        if (aux[mid - 1] <= aux[mid] and aux[mid + 1] <= aux[mid]):
            return aux[mid]
        elif (aux[mid] < aux[mid + 1]):
            return find_peak(aux[mid + 1:])
        else:
            return find_peak(aux[:mid - 1])
