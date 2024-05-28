#!/usr/bin/python3
"""Def of function pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of int representing a Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle_num = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle_num[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle_num.append(row)
    return triangle_num
