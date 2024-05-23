#!/usr/bin/python3
"""function returns True if object is an instance of the class"""


def is_same_class(obj, a_class):
    """return True or False"""
    if not type(obj) == a_class:
        return False
    else:
        return True
