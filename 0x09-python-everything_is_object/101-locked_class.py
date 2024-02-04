#!/usr/bin/python3
"""Reps a class that doesn't allow users create class/obj attributes"""


class LockedClass:
    """Defines the class LockedClass"""

    __slots__ = ['_first_name']

    def __init__(self):
        """Initializes the class"""
        self.first_name = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
