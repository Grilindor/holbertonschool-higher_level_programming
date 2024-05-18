#!/usr/bin/python3

"""
class definition of 'Square'
"""

class Square:
    """ a defined square"""
    def __init__(self, size):
        # Initialize the Square class with a given size
        self._Square__size = size

    def __init__(self, size=0):
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
