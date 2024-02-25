#!/usr/bin/python3

"""This represents a function that divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix and prints out a new matrix set.

    Args:
        matrix (list of lists): A matrix (list of lists) contains int, float.
        div (int, float): the divisor.

    Returns:
        list of lists: A new matrix with elements divided by `div`,
                       rounded to two decimal places
    Raises:
        TypeError: If `matrix` is not a valid matrix of integers and floats.
                   If `div` is not a number.
                   If each row of the matrix does not have the same size.
        ZeroDivisionError: If `div` is equal to zero.
    """

    new_matrix = []
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float))
                   for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
