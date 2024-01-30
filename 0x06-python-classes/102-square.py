#!/usr/bin/python3

"""This comment defines a class Square."""


class Square:
    """This class depicts a square wit size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the field size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square."""
        return (self.__size * self.__size)

    def __eq__(self, next_sq):
        """Checks == comparison to a Square instance"""
        return self.area() == next_sq.area()

    def __ne__(self, next_sq):
        """Checks != comparison to a Square instance"""
        return self.area() != next_sq.area()

    def __lt__(self, next_sq):
        """Checks < cmparison to a square instance"""
        return self.area() < next_sq.area()

    def __le__(self, next_sq):
        """Checks <= comparison to a squre instance"""
        return self.area() <= next_sq.area()

    def __gt__(self, next_sq):
        """Checks > comparison to a square instance"""
        return self.area() > next_sq.area()

    def __ge__(self, next_sq):
        """Checks >= comparison to a square instance"""
        return self.area() >= next_sq.area()
