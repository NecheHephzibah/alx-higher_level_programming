#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix:
        new_matrix = matrix.copy()
        for row in matrix:
            new_matrix[row] = list(map(lambda x: x**2, matrix[row]))
    return (new_matrix)
