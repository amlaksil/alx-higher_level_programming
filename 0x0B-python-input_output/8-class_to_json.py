#!/usr/bin/python3
"""
This module contains a function called
`class_to_json` that takes one argument
which is an instance of a class and returns
the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Return dictionary description
    Args:
        obj (obj): an instance of a class
    Return:
        dictionary description
    """
    return obj.__dict__
