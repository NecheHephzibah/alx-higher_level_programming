#!/usr/bin/python3
"""Represents a module containing a class"""


class Student:
    """Defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialises the class with constructor and attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Defines a public method that retrieves a dict. rep. of Student"""
        return self.__dict__
