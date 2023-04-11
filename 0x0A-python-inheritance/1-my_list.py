#!/usr/bin/python3
"""This module contains a class called `MyList`
that inherits a list object
"""


class MyList(list):
    """Inherits list form list
    """
    def print_sorted(self):
        """It prints an integer list in sorted order
        (ascending sort)
        """
        list_cpy = super(MyList, self).copy()
        print(sorted(list_cpy))
