#!/usr/bin/python3
"""
This moudle contains a function called
`is_same_class` which checks whether a particular
object is belong to the specified class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of
    the specified class otherwise False
    Args:
        obj (object): object
        a_class (class): class
    Return: True if the object is belong of the specified class
            otherwise False
    """
    if a_class == object:
        return False
    return isinstance(obj, a_class)
