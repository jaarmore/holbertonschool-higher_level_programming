#!/usr/bin/python3
"""
This module contains say_my_name function.
Prototype def def say_my_name(first_name, last_name="").
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>

    Args:
        first_name: the first name to print
        last_name: the last name to print

    Returns: Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('first_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
