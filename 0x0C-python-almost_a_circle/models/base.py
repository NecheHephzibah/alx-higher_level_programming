#!/usr/bin/python3
"""Represents a module containing class called Base"""

import json


class Base:
    """Defines a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Defines the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

        return

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defines a static method"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        filename =  cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []

        with open(filename, "w") as f:
            json_str = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation json_string"""

        if json_string is None or json_string is []:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (pointer): Double pointer to a dictionary.

        Returns:
            An instance with all attributes already set.
        """
