#!/usr/bin/python3
"""
This moudle consists of a function called
`from_json_string` that imports JSON module and
returns an object (python data structure)
"""
import json


def from_json_string(my_str):
    """Convert JSON file to python data structure
    Args:
        my_str (JSON): JSON string
    Return:
        object (python data structure)
    """
    return json.loads(my_str)
