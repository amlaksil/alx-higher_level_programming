#!/usr/bin/python3
"""A module that defines a square class"""


class Square:
    """A square calass that defines size, calculate the area of the square,
      and print the square in hash(#) table format
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing square class

        Args:
            size (int): the size of the square
            position (tuple): a position where lines filled by space
            when position[1] > 0 don't fill lines by space
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        # Use property setter to invoke validation
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """Getter method which retrieves tuple and the setter method sets
           the right tuple. Position must be a tuple of 2 positive integers
           otherwise raise a TypeError.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not\
           all(isinstance(v, int) for v in value) or any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of square which is the square of its length """
        return int(self.__size) ** 2

    def __str__(self):
        """Return a string representation of the object.
        The string representation consists of a square shape made
        up of '#' characters, with an optional leading newline character
        and indentation based on the position.

        Returns:
            str: String representation of the object.
        """
        size = self.size
        position = self.position
        new_line = fstr = chars = ''
        count_spaces = 0
        data = []
        if size == 0:
            return '\n'
        else:
            if position[1] > 0:
                for _ in range(position[1]):
                    new_line += '\n'
            for _ in range(size):
                if not (position[1] > 0):
                    count_spaces += position[1]
                count_spaces += position[0]
                chars += size * "#" + '\n'
                data.append(count_spaces * " " + chars)
                count_spaces = 0
                chars = ''
        for i in range(len(data)):
            fstr += data[i]
        fstr = fstr[:len(fstr) - 1]
        return new_line + fstr

    def my_print(self):
        """If size is not zero it prints n by n (n x n) '#' table
        otherwise it prints empty line
        """
        size = self.size
        position = self.position
        if size == 0:
            print()
        else:
            if position[1] > 0:
                print('\n' * position[1], end="")
            for i in range(1, size + 1):
                if not (position[1] > 0):
                    print(position[1] * " ", end="")
                print(position[0] * " ", end="")
                print(size * "#")
