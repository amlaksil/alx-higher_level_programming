#!/usr/bin/python3
"""This module contains a `Rectangle` class which is
sub class of `Base` class
"""
from .base import Base


class Rectangle(Base):
    """A Rectangle class that inherits `id` from Base class and defines
    an init constructor whih consists four private instance attributes and
    one inherited attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize arguments of the function
        Args:
            width (int): width of the rectangle
            height (int): height of ther rectangle
            x (int): an integer variable
            y (int): an integer variable
            id (int):  an integer variable inherited from Base class
        """
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Returns formated string representation of an object """
        str1 = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        str2 = " - {}/{}".format(self.__width, self.__height)

        return str1 + str2

    @property
    def width(self):
        """Returns the right value for width of rectangle which is setted by
        the setter method
        Args:
            value (int): a value to be checked
        Raises:
            TypeError: if the width is not integer
            ValueError: if the width less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(f"{'width'} must be an integer")
        if value <= 0:
            raise ValueError(f"{'width'} must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the right value for height of rectangle which is setted
        by the setter method
        Args:
            value (int): a value to be checked
         Raises:
            TypeError: if the height is not integer
            ValueError: if the height less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError(f"{'height'} must be an integer")
        if value <= 0:
            raise ValueError(f"{'height'} must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the right value for x which is setted by
        the setter method
        Args:
            value (int): a value to be checked
        Raises:
            TypeError: if x is not integer
            ValueError: if x is not less than or equals to zero
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError(f"{'x'} must be an integer")
        if value < 0:
            raise ValueError(f"{'x'} must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the right value for y which is setted by
        the setter method
        Args:
            value (int): a value to be checked
        Raises:
            TypeError: if y is not integer
            ValueError: if y is not less than or equals to zero
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError(f"{'y'} must be an integer")
        if value < 0:
            raise ValueError(f"{'y'} must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """Prints rectangle to stdout"""
        w = self.__width
        h = self.__height
        for l in range(self.__y):
            print()
        for i in range(h):
            print("{}{}".format(self.__x * " ", w * '#'))

    def update(self, *arg, **kwargs):
        """Update the value of arguments defined in the init
        constructor method based on the order specified below
        Args:
            args (int): variable number of arguments. This type of argument is
                        called no-keyword argument. Argument order is important
            kwargs (int): double pointer to a dictionary key/value pair
            kwargs is not literally a double pointer - describing it as such
            make things easy to understand. This type of argument is called
            key-worded argument. Argument order is not important
        """
        num_arg = len(arg)
        if num_arg == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    elif key == 'width':
                        self.__width = value
                    elif key == 'height':
                        self.__height = value
                    elif key == 'x':
                        self.__x = value
                    elif key == 'y':
                        self.__y = value
        while True:
            if num_arg == 0:
                break
            self.id = arg[0]
            if num_arg == 1:
                break
            self.__width = arg[1]
            if num_arg == 2:
                break
            self.__height = arg[2]
            if num_arg == 3:
                break
            self.__x = arg[3]
            if num_arg == 4:
                break
            self.__y = arg[4]
            break

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        the dicionary must contain id, width, height, x and y parametrs
        """
        h = self.__height
        w = self.__width
        dict_ = {"x": self.__x, "y": self.__y, "height": h, "width": w}

        return dict_
