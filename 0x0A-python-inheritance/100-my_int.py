#!/usr/bin/python3
"""
This moudle only contains a class
called 'MyInt' which inherits from int
"""


class MyInt(int):
    """MyInt class inherits form int
    """
    def __eq__(self, other):
        """Invert == to != """
        return False

    def __ne__(self, other):
        """Invert != to == """
        return True
