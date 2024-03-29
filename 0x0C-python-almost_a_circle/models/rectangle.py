#!/usr/bin/python3
"""Represents a subclass Rectangle"""

from models.base import Base


class Rectangle(Base):
    """
    Defines a subclass Rectangle that inherits from class Base.
    Inherited Attributes:
        id

    Class Attributes:
       width
       height
       x
       y

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args, **kwargs);  width(self); width(self, value)
        height(self); height(self, value); x(self); x(self, value)
        y(self); y(self, value); area(self); display(self)
        __str__; to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner of the rectangle.
            y (int): The y-coordinate of the top-left corner of the rectangle.
            id (int): The id of the rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets/Sets the width of a rectangle"""
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
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character "#" to stdout"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            # Print spaces for x-coordinate offset
            print(" " * self.x, end="")

            # print '#' for the width of the rectangle
            print("#" * self.width)

    def __str__(self):
        """
        Defines the string representation of the Rectangle subclass
        returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>

        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y, self.__width,
                        self.__height))

    def update(self, *args, **kwargs):
        """
        Assign an attribute.

        Args:
            *args (positional argument): assigns argument variables by index.
            **kwargs (keyword argument): assigns argument by their keys.

        """
        if args and len(args) > 0:
            self.id = args[0] if len(args) >= 1 else self.id
            self.__width = args[1] if len(args) >= 2 else self.__width
            self.__height = args[2] if len(args) >= 3 else self.__height
            self.__x = args[3] if len(args) >= 4 else self.__x
            self.__y = args[4] if len(args) >= 5 else self.__y
        else:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """
        Defines a diction representation of the subclass Rectangle.

        Returns:
            The dictionary representation of a Rectangle.
        """

        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
