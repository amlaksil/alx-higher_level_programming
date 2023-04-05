#!/usr/bin/python3
"""A simple module that contains only one
function ``add_integer()`` that adds two
numbers if the number are float or int otherwise
it will raises an error.
"""


def add_integer(a, b=98):
    """Adds two integer number and retuns the result
    Args:
        a (int): the first number
        b (int): second number
    Raises:
        TypeError: if the numbers are not integer or float
    Return:
        the sum of the two number
    """
    if type(a) is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
