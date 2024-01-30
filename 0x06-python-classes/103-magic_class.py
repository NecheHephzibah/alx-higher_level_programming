#!/usr/bin/python3

"""Represents a class called MagicClass"""
import math


class MagicClass:
    """Defines a Circle"""

    def __init__(self, radius=0):
        """Initialize MagicClass.


        Arg:
            radius (float or int): The radius of the MagicClass(circle).
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of a circle"""
        return (2 * math.pi * self.__radius)
