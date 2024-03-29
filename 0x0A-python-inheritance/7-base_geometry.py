#!/usr/bin/python3
"""
This module defines 'BaseGeometry' class
that contains area and integer_validator
method
"""


class BaseGeometry:
    """A BaseGeometry class that defines two methods """
    def area(self):
        """Raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed
        Args:
            name (str): is always string
            value (int): is an integer
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
