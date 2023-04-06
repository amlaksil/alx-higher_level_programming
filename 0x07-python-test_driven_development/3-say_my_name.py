#!/usr/bin/python3
"""
This module contains only one functon
``say_my_name`` which prints the first and last
name of user
"""


def say_my_name(first_name, last_name=""):
    """Prints the user first name and last name
    Args:
        first_name (str): first name of the user
        last_name (str): last name of the user
    Raises:
        TypeError: If the firs_name or last name given
                   is not string
    """
    if isinstance(first_name, str) is not True\
       or first_name.isalpha() is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
