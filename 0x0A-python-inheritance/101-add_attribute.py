#!/usr/bin/python3
"""
This module contains a function called
`add_attribute` that adds new attribute
to an object it it's possible.
"""


def add_attribute(self, name, value):
    """Add a new attribute to an object if it's possible
    Args:
        name (str): name of variable
        value (str): value to name
    """
    if hasattr(self, '__dict__'):
        self.name = value
    else:
        raise TypeError("can't add new attribute")
