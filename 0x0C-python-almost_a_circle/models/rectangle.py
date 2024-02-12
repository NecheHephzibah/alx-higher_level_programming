#!/usr/bin/python3
"""Represents a subclass Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines the subclass Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): The id of the rectangle.
        """
        super().__init__(id)
        self.__width =  width
        self.__height = height
        self.__x = x
        self.__y = y
