#!/usr/bin/python3
"""File contains a class named Rectangle"""


class Rectangle:
    """Represents a Rectangle.

    Attributes:
        number_of_instances (int): The number of rectangle instances.
        print_symbol (any type): Symbol used for string representation,
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = []
            for i in range(0, self.__height):
                for j in range(self.__width):
                    result.append(str(self.print_symbol))
                if i != self.__height - 1:
                    result += '\n'
        return ("".join(result))

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        representation = "Rectangle(" + str(self.__width)
        representation += ", " + str(self.__height) + ")"
        return representation

    def __del__(self):
        """Deletes the instance of the rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2
