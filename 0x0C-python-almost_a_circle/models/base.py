#!/usr/bin/python3
"""Represents a module containing class called Base"""

import json
import csv
from io import StringIO


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
        """Defines a static method, that converts dictionaries to json str"""

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
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []

        with open(filename, "w") as f:
            json_str = cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation json_string"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (dict): Dictionary containing attribute values.

        Returns:
            An instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + '.json'
        instance_list = []

        try:
            with open(filename, "r") as f:
                json_data = f.read()
                data_list = cls.from_json_string(json_data)
                for data in data_list:
                    instance = cls.create(**data)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV representation of list_objs to a file.
        CSV stands for  Comma Separated Values. It's a simple file 
        format used to store tabular data, such a s a spreadsheet or database.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + '.csv'

        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads data from a CSV file and returns a list of dictionaries."""
        filename = cls.__name__ + '.csv'

        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                reader = csv.DictReader(f, fieldnames=fieldnames)
                reader = [dict([row, int(v)] for row, v in diction.items())
                                for diction in reader]
                return [cls.create(**diction) for diction in reader]
        except IOError:
            return []
