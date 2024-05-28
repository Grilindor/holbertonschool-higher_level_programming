#!/usr/bin/env python3
"""
    custom Python class named CustomObject
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """save Python Dictionary in pickle file"""
        with open(filename, mode="wb") as file2_toread:
            pickle.dump(self, file2_toread)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file6_toread:
            return pickle.load(file6_toread)
