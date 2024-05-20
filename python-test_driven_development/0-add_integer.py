#!/usr/bin/python3
""" Return the addition of two integer
>>> add_integer(5, 10)
15
>>> add_integer(2)
100"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod(add_integer.txt)
