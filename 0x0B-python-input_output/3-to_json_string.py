#!/usr/bin/python3
"""
This moudle consists of a function called
`to_json_string` that imports JSON module and
returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Change the object to JSON
    Args:
        my_obj (obj): object (string)
    Return:
        the JSON representation of an object
    """
    return json.dumps(my_obj)
