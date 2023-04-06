#!/usr/bin/python3
"""
This mudule consists of the ``print_square``
function which prints a square with the
character `#`

"""


def print_square(size):
    """Prints a square with the character `#`
    Args:
        size (int): the size of the square to be printed
    Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than zero it must be >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * '#')
