#!/usr/bin/python3

def matrix_divided(matrix, div):
    martrix_list = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(martrix_list)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    len_ref = len(matrix[0])
    for row in matrix:
        if len(row) != len_ref:
            raise TypeError("Each row of the matrix must have the same size")

    div_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]

    return div_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod(matrix_divided.txt)
