#!/usr/bin/python3
"""
Function that read a text file
"""


def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a text file

    Args:
        filename: name of the file
        nb_lines: number of lines to read
    """
    tlines = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            tlines += 1

    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0 or nb_lines >= tlines:
            print(a_file.read())
        else:
            for line in range(nb_lines):
                print(a_file.readline(), end='')
