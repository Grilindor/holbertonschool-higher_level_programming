#!/usr/bin/python3

"""
Prints a matrix of integers.

Parameters:
- matrix: A matrix of integers

Returns:
The matrix printed
"""

def print_matrix_integer(matrix=[[]]):
        for row in range(len(matrix)):
                for column in range(len(matrix[row])):
                        print("{:d}".format(matrix[row][column]), end="")
                        if column != len(matrix[0]) - 1:
                                print(" ", end="")
                print("")

