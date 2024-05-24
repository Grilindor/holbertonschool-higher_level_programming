#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
