#!/usr/bin/python3
"""This module contains a class called
`Base`
"""


class Base:
    """This class defines a private class attribute
    and class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id if it is not None
        Args:
            id (int): public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
