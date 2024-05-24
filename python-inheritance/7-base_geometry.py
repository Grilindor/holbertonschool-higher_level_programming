#!/usr/bin/python3
"""class of BaseGeometry"""


class BaseGeometry:
    """Public instance method raises an Exception with a message"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
