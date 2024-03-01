#!/usr/bin/python3
"""
This module imports `Rectangle` class from `9-rectangle.py` and
defines `Square` class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle class."""
    def __init__(self, size):
        """
        Initialize the size of square.

        Args:
            size (int): The size of square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """
        Calculates the area of square.
        """
        return self.__size ** 2
