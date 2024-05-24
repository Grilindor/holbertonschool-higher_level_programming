#!/usr/bin/python3
"""class of BaseGeometry"""


class BaseGeometry:
    """Public instance method raises an Exception with a message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
