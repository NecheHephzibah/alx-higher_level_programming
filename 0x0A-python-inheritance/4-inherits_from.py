#!/usr/bin/python3
"""Represents a module containing a function that checks instances"""


def inherits_from(obj, a_class):
    """
    Defines a function that checks if the object is an instance of
    a class taht inherited directly or indirectly form the specified
    class.

    Args:
        obj (object): a variable containing whatever is assigned to it.
        a_class (type): data type

    Returns:
        True: If the object is a direct instance of the class.
        False: If the object is not.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
