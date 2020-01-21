#!/usr/bin/python3
"""
Lookup function Module
"""


def lookup(obj):
    """
    Function that return the list of available attributes
    and methods of an object.
    """
    return (dir(obj))
