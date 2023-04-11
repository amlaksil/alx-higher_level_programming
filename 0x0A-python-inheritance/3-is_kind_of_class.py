#!/usr/bin/python3
"""
This moudle contains only a single function
called `is_kind_of_class`
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is
    an instance of a class that inherited form, specified class; otherwise
    False
    Args:
        obj (object): object
        a_class (class): class
    Return: True if an object is an instance of a specified class else False
    """
    return isinstance(obj, a_class)
