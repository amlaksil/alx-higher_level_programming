#!/usr/bin/python3
"""This module consists of a class called
`Square` which is a subclass of `Rectangle` class
"""
import ast
from .rectangle import Rectangle


class Square(Rectangle):
    """This class is a subclass of Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize arguments
        Args:
            size (int): size of square
            x (int): integer variable
            y (int): integer variable
            id (int): an integer number inherited from super class
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        str1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        str2 = " - {}".format(self.size)

        return str1 + str2

    @property
    def size(self):
        """This getter method retrieve the size of the square/width and
        the setter sets the right value for the size of square
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size less than zero
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the value of arguments defined in the init
        constructor method based on the order specified below
        Args:
            args (int): variable argument (none-keyword arguments)
            kwargs (dict): key/value pair (keyworded arguments)
        """
        num_arg = len(args)
        if num_arg == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value

        while True:
            if num_arg == 0:
                break
            self.id = args[0]
            if num_arg == 1:
                break
            self.size = args[1]
            if num_arg == 2:
                break
            self.x = args[2]
            if num_arg == 3:
                break
            self.y = args[3]
            break

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.
        This dictionary contains id, size, x, and y
        """
        dict1 = "{}'{}': {}, '{}': ".format('{', 'id', self.id, 'x')
        dict2 = "{}, ".format(self.x)
        dict3 = "'{}': {}, '{}': {}".format('size', self.size, 'y', self.y)

        return ast.literal_eval(dict1 + dict2 + dict3 + '}')
