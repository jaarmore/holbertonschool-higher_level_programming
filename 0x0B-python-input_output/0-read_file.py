#!/usr/bin/python3
"""
Function that reads a text file encoding UTF-8
"""


def read_file(filename=""):
    """
    Function that reads a text file
    Args:
        filename: name of the file
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
