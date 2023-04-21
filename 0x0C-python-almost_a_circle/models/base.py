#!/usr/bin/python3
"""This module contains a class called `Base` """
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (dict): is a list of dictionaries
        Return:
            if it is empy or None, return the string: '[]'
            otherwise, return the JSON string representation
            of list_dictionarie
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (object): list of instance - JSON object
        description: If list_objs is None, save an empty list.
        The filename must be <Class name>.json
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation of json_string
        Args:
            json_strin - is a string representing a list of dictionaries
        Return:
            list of JSON string rep
        """
        if json_string is None:
            return []
        json_str_list = json.loads(json_string)
        return json_str_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary:  can be thought of as a double pointer to a dictionary
        Return:
            instance
        """
        if cls.__name__ == "Rectangle":
            new = cls(12, 10)
        else:
            new = cls(1)
        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        description:
            filename must be <Class name>.json
            If the file doesn't exist return an empty list
            we have to use previously implemented methods which are
            from_json_string and create
        """
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename) is not True:
            return []

        with open(filename, encoding="utf-8") as f:
            contents = f.read()
            json_list = cls.from_json_string(contents)
            list_instances = []
            for i in range(len(json_list)):
                list_instances.append(cls.create(**json_list[i]))
        return list_instances
