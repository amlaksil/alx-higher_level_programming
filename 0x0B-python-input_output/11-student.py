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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
           attrs (list): list of string
        Return:
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved. Otherwise, all attributes must
            be retrieved
        """
        dictnry = {}
        if type(attrs) is list:
            for attr in self.__dict__:
                if attr in attrs:
                    dictnry[attr] = self.__dict__[attr]
            return dictnry
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attribute of the `Student` instance
        Args:
            json (JSON): dictionary
        """
        self.__dict__ = json
