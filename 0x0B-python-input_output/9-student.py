#!/usr/bin/python3
"""
This module contains a class called
`Student` that takes first_name, last_name,
and age as public attributes and contains
a method `to_json` that retrieves a dictionary
representation of a `Student` instance
"""


class Student:
    """A Student class that defines first name, last name, age, and
    a method `to_json` which retrieves a dictionary representation of
    the class
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the variable
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
