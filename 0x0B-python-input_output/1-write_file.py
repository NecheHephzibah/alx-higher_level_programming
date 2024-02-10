#!/usr/bin/python3
"""Represents function that writes a sstring to a text file."""


def write_file(filename="", text=""):
    """
    Defines the function that writes to a string

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        The number of characters written.
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
