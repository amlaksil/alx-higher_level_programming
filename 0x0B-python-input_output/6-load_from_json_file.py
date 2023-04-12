#!/usr/bin/python3
"""
This module consists of a function called
`load_form_json_file` that loads JSON data
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename (str): the name of the file
    Return:
        created object
    """
    with open(filename, 'r', encoding="utf-8") as file_1:
        return json.load(file_1)
