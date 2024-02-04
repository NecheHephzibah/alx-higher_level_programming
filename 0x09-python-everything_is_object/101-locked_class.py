#!/usr/bin/python3
"""Reps a class that doesn't allow users create class/obj attributes"""


class LockedClass:
    """Defines the class LockedClass"""

    __slots__ = ['first_name']

    def __init__(self):
        """Initializes the class"""
        self.first_name = None

    def __setattr__(self, name, value):
        """Overiides the default setattr behaviour"""
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
        else:
            self.__dict__[name] = value

