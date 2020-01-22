#!/usr/bin/python3
"""
Function that returns a numbers of lines of file
"""


def number_of_lines(filename=""):
    """
    Function that returns the numbers of lines of text file
    Args:
        filename: name of the file

    Returns:
        The number of lines of text file
    """
    lnumber = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            lnumber += 1
        return lnumber
