#!/usr/bin/python3
"""Represents a module containing class called Base"""


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
