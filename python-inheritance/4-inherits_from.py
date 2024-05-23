#!/usr/bin/python3
"""function inherits_from"""


def inherits_from(obj, a_class):
    """unction that returns True if the object is
    an instance of a class that inherited"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
