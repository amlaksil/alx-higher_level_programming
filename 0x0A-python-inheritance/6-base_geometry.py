#!/usr/bin/python3
"""
This module consists of a class 'BaseGeometry'
that defines a public instance method called area
which raises an Exception
"""


class BaseGeometry:
    """A class that defines a public instance method called area
    """
    def area(self):
        """Raise Exception """
        raise Exception("area() is not implemented")
