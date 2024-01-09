#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for inner_row in row:
                print("{:d}".format(inner_row), end=" "
                      if inner_row != row[-1] else "")
            print()
