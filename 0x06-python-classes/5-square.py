#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A square calass that defines size, calculate the area of the square,
      and print the square in hash(#) table format
    """
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
        """This getter method retrieves the size and the setter method sets
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

    def my_print(self):
        """If size is not zero it prints n by n (n x n) '#' table
        otherwise it prints empty line
        """
        n = int(self.__size)
        if n == 0:
            print()
        else:
            for i in range(1, n + 1):
                print(n * "#")
