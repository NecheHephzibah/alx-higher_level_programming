#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not all(matrix):
        return

    num_row = len(matrix)
    num_col = len(matrix[0])
    trans_matrix = []
    for i in range (num_col):
        trans_matrix.append([row[i] for row in matrix])

    for row in trans_matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
