#!/usr/bin/python3

"""
class definition of 'Square'
"""


class Square:
    """ a defined square"""
    def __init__(self, size=0):
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        # calculates and returns the area of the square
        return self.__size * self.__size
