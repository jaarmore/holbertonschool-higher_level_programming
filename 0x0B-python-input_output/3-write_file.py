#!/usr/bin/python3
"""
Function that write on a text file
"""


def write_file(filename="", text=""):
    """
    Function that write a string on text file

    Args:
        filename: name of the file
        text: string to write in text file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        cwritten = a_file.write(text)
    return cwritten
