#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class Student, Public instance attributes"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method"""
        return self.__dict__
