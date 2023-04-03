#!/usr/bin/python3
"""This module defines Rectangle class"""


class Rectangle:
    """A class that defines width and height of the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the width and height of the rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """This getter method retrieve the width of the rectangle and
            the setter sets the right value for width
            Raises:
                TypeError: if the given width is not integer
                ValueError: if the given width less than zero
            """
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """This getter method retrieve the height of the rectangle and
            the setter sets the right value for the height
            Raises:
                TypeError: if the height is not integer
                ValueError: if the height less than zero
            """
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
