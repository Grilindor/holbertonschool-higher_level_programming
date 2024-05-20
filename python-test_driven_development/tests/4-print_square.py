#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    # size be an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    # size not float, no less than 0
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    # print the square
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testmod(print_square.txt)

