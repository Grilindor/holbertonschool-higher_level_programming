#!/usr/bin/python3
"""
In this class, we have a private instance attribute
__size
that represents the size of the square. The
__init__
method is used for instantiation with the size provided. We also have a
property size
to access the size attribute and a setter method to update the size if needed.
The area
method calculates and returns the area of the square.
"""


class Square:
    """ a defined square"""
    def __init__(self, size):
        self._Square__size = size


