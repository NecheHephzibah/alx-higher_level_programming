#!/usr/bin/python3
"""Represents a function that prints new lines after punctuations"""


def text_indentation(text):
    """
    Defines a function that takes a text of string and prints new lines
    when punctuation (. : ?) are encountered.

    Args:
        text (str): The text provided by the user.

    Returns:
        Prints/returns the edited text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [char.strip(" ") for char in text.split(delim)])
    print(text, end="")



if __name__ == "__main__":
    import doctest
    doctest.testfile(tests/5-text_indentation.txt)
