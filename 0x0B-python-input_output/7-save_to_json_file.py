#!/usr/bin/python3
"""
Function that writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file

    Args:
        my_obj: object to write
        filename: name of file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
