#!/usr/bin/python3
"""Represents a module that prints a square with the character #"""


def print_square(size):
    """
    Defining a function that prints a Square.

    Args:
        size (int): Integer argument passed depicting the length
                    and breadth of the square.

    Returns:
        The pictorial form of size.

    Raises:
        TypeError: If size is not an integer.
                   If size is float and is less than zero.
        ValueError: If size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print('#', end='')
        print()


if __name__ == "__maiin__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
