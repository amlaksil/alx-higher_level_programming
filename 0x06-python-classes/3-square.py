#!/usr/bin/python3
"""A module that define a square """


class Square:
    """square class that defines size of the square (square object) """
    def __init__(self, size=0):
        """Initializing square class

        Args:
            size (int): the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Returns the area of square which is the square of its length """
        return int(self.__size) ** 2
