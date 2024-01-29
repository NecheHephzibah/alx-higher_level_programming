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

    def my_print(self):
        """Prints the square using #""" 
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
