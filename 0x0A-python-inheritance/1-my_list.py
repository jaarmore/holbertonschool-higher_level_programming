#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """
    Function that prints a list in ascending sort.
    """"
    def print_sorted(self):
        print(sorted(self))
