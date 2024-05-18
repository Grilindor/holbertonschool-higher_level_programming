#!/usr/bin/python3
"""
class definition of 'Square'
"""


class Square:
    """ a defined square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # calculates and returns the area of the square
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("\n")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print(end="\n")
