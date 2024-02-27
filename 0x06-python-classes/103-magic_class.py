#!/usr/bin/python3
"""
This module contains a MagicClass for performing calculations on circles.
"""
import math


class MagicClass:
    """
    A magical class for performing calculations on circles.
    """
    def __init__(self, radius):
        """
        Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return self.__radius * 2 * math.pi
