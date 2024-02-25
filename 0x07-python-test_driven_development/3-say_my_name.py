#!/usr/bin/python3
"""This module contains a function that prints strings."""


def say_my_name(first_name, last_name=""):
    """
    Defines a function that receives two strings and prints them out.

    Args:
        first_name (str): The first argument to the function.
        last_name (str): The second argumnet to the function.

    Returns:
        Prints an output with the arguments.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
