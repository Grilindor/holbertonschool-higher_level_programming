#!/usr/bin/python3
"""
class definition of 'Square'
"""


class Square:
    """ a defined square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and\
            type(value[0]) is int and type(value[1]) is int and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        # calculates and returns the area of the square
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
