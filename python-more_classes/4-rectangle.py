#!/usr/bin/python3
""" Contains a class definition of 'Rectangle' """

from typing import Any


class Rectangle:
    # a defined rectangle
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Check if value is greater than or equal to 0
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if value is greater than or equal to 0
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        # return perimeter of rectangle
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

# print the rectangle with the character #
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        else:
            for i in range(self.__height):
                for j in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width
