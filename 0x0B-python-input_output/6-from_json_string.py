#!/usr/bin/python3
import json
"""
6. From JSON string to Object
"""


def from_json_string(my_str):
    """
    function that returns an object represented by a JSON string
    """
    return json.loads(my_str)
