#!/usr/bin/python3
"""
In this class, we have a private instance attribute
_Square__size
that represents the size of the square. The
__init__
method is used for instantiation with the size provided. We also have a
property : size
"""


class Square:
    """ a defined square"""
    def __init__(self, size):
        # Initialize the Square class with a given size
        self._Square__size = size
