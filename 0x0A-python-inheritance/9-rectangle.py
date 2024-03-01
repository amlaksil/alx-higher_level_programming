#!/usr/bin/python3
"""
This module imports `BaseGeometry` class
form '7-base_geometry.py` and defines `Rectangle` class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a subclass of BaseGeometry class """
    def __init__(self, width, height):
        """Initialize the value of width and height
        Args:
           width (int): width of rectangle
           height (int): height of rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns formated string."""
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'

    def area(self):
        """
        Calculates the area of a rectangle.
        """
        return self.__width * self.__height
