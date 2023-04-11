#!/usr/bin/python3
"""
This module consists of a function called
`inherits_from`
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj (object): object
        a_class (class): class
    Return:
          Returns True if the object is an instance of a class that inherited
          (directly or indirectly) from the specified class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
