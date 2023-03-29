#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """square class that defines size and calculate the area of square """
    def __init__(self, size=0):
        """Initializing square class

        Args:
            size (int): the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.__size = size

    @property
    def size(self):
        """This getter method retrieves the size and the setter method sest
        the right value for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of square which is the square of its length """
        return int(self.__size) ** 2
