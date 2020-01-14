#!/usr/bin/python3
"""
This module contains print_square function.
Prototype def print_square(size)
Function that prints a square.
"""


def print_square(size):
    """
    function that prints a square with the character #.

    Args:
        size: size of square to print

    Returns:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for elem in range(size):
        print('{}'.format('#' * size))
