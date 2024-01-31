#!/usr/bin/python3

"""File contains a class named Rectangle"""


class Rectangle:
    """Represents a Rectangle, sort of an empty class"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets and sets the value for width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets and sets the value for height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Gets the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width + 2 * self.height)

    def __str__(self):
        """Prints the rectangle and also calls the str()"""
        result = ""
        if self.__width == 0 and self.__height == 0:
            return result
        else:
            for i in range(0, self.__height):
                for j in range(self.__width):
                    result += "#"
                result += '\n'
        return result
