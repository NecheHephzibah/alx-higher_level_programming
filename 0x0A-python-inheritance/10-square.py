#!/usr/bin/python3

"""Represents a module containing a class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Defines a public method instance"""
        return

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a child class Rectangle that inherits from parent class"""

    def __init__(self, width, height):
        """Defines a child class Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Defines a public method instance area"""
        return self.__width * self.__height

    def __str__(self):
        """Defines the string representation of the object"""
        string = "[" + str(self.__class__.__name__) + "]"

        string += str(self.__width) + "/" + str(self.__height)

        return string


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
