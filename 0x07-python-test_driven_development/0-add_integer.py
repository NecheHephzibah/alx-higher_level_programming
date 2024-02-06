#!/usr/bin/python3

"""This module provides function that adds 2 integers"""

def add_integer(a, b=98):
    """
    Calculate the sum of a and b.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
    int: The sum of `a` and `b`

    Raises:
    TypeError: If a or b is not an integer or float.
    OverflowError: If infinity is provided as an argument.
    ValueError: If NaN (Not-a-Number) is provided as an argument.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return  a + b
