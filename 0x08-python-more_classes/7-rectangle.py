#!/usr/bin/python3
"""This module defines Rectangle class"""


class Rectangle:
    """A class that defines width and height of the rectangle and calculates
    the area and perimeter of the rectangle
    Args:
        number_of_instances (int): puplic class attribute that counts each
    instance instantiation and incremented during each instance instantiation
    and decremented during each instance deletion
        print_symbol (char): can be any type
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the width and height of the rectangle.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """prints a character rectangle """
        n = self.__width
        m = self.__height
        symbol = self.print_symbol

        if n != 0 and m != 0:
            for i in range(m):
                if i != m - 1:
                    print("{}".format(n * symbol))
                if i == m - 1:
                    print("{}".format(n * symbol), end="")
        return f""

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    @property
    def width(self):
        """This getter method retrieve the width of the rectangle and
        the setter sets the right value for width
        Raises:
            TypeError: if the width is not integer
            ValueError: if the width less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        "Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        """Is a destructor method which is called as soon as all references
        of the object are deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
