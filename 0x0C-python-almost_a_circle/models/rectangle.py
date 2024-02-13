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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Defines the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character "#" to stdout"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            # Print spaces for x-coordinate offset
            print(" " * self.__x, end="")

            # print '#' for the width of the rectangle
            print("#" * self.__width)

    def __str__(self):
        """Defines the string representation of the Rectangle subclass"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,\
self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """Assigns an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0] if len(args) >= 1 else self.id
            self.__width = args[1] if len(args) >= 2 else self.__width
            self.__height = args[2] if len(args) >= 3 else self.__height
            self.__x = args[3] if len(args) >= 4 else self.__x
            self.__y = args[4] if len(args) >= 5 else self.__y
