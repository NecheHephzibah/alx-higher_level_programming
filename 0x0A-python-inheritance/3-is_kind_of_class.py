#!/usr/bin/python3
"""Represents a module containing a function that checks instances"""


def is_kind_of_class(obj, a_class):
    """
    Defines a function that checks the instance of an object.

    Args:
        obj (object): a variable containing whatever is assigned to it.
        a_class (type): data type

    Returns:
        True: If the object is a direct instance of the class.
        False: If the object is not.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
