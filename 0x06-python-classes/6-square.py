#!/usr/bin/python3
"""A module that defines a square """


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
        self.__size = size
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
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method which retrieves tuple and the setter method sets
           ther right tuple. Position must be a tuple of 2 positive integers
           otherwise raise a TypeError
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of square which is the square of its length """
        return int(self.__size) ** 2

    def my_print(self):
        """If size is not zero it prints n by n (n x n) '#' table
        otherwise it prints empty line
        """
        n = int(self.__size)
        py = int(self.__position[1])
        px = int(self.__position[0])
        if n == 0:
            print()
        else:
            if py > 0:
                print()
            for i in range(1, n + 1):
                if not (py > 0):
                    print(py * " ", end="")
                if px > 0:
                    print(px * " ", end="")
                print(n * "#")
