#!/usr/bin/python3
"""Represents a sub-subclass Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the sub-subclass Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the top-left corner of the square.
            y (int): The y-coordinate of the top-left corner of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets and sets size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Defines the string representation of the Square.

        Returns:
            str: A formatted string representing the Square.
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
           *args (positional argument): assigns argument variables by index.
           **kwargs (keyword argument): assigns argument by their keys.

        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('size', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Defines the dictionary representation of the sub-subclass Square.

        Returns:
            The dictionary representation of the sub-subclass Square.
        """
        return {
            'id' : self.id,
            'size' : self.width,
            'x' : self.x,
            'y' : self.y
        }