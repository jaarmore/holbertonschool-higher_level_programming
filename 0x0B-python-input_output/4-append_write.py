#!/usr/bin/python3
"""
Function that appends on a text file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string on text file

    Args:
        filename: name of the file
        text: string to append in text file
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        cappend = a_file.write(text)
    return cappend
