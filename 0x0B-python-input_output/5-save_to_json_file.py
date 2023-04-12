#!/usr/bin/python3
"""
This module contains a function called
`save_to_json_file` that writes an object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes JSON object to a file
    Args:
        my_obj (obj): object to be written
        filename (json) : name of the file
    """
    with open(filename, mode='w', encoding="utf-8") as file_1:
        json.dump(my_obj, file_1)
