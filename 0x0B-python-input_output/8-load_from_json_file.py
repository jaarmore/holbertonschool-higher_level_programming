#!/usr/bin/python3
import json
"""
Function that creates an Object from JSON
"""


def load_from_json_file(filename):
    """
    Function that creates an Object from JSON file

    Args:
        filename: name of file
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
