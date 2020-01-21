#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
