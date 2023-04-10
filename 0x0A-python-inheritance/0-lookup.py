#!/usr/bin/python3
"""This module contains function called
`lookup` which returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    Args:
        obj (object): object to be passed
    """
    return dir(obj)
