#!/usr/bin/python3
"""a class Student that defines a student by: (based on 9-student.py)"""


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

    def to_json(self, attrs=None):
        """Public method, that retrieves a dictionary of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Public method that replaces all attributes of Student instance"""
        for i in json:
            self.__dict__[i] = json[i]
