#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = [[0] * len(row) for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            square_matrix[row][column] = pow(matrix[row][column], 2)
    return square_matrix

# second possibility
# return ([list(map(lambda x: x ** 2, row)) for row in matrix])
