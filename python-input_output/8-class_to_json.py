#!/usr/bin/python3
"""
    a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """return dictionnari of all objet"""
    dictionary = {}
    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()

    return dictionary
