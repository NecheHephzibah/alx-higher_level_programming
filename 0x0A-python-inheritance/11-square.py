#!/usr/bin/python3

"""Represents a module containing a class BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a grandchild class that inherits from rectangle child class"""

    def __init__(self, size):
        """
        Defines a method with size argument.

        Arg:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
