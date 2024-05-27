#!/usr/bin/python3
"""
    a function that writes an Object to a text file,
    using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file with json"""
    with open(filename, "w") as file5_toread:
        json.dump(my_obj, file5_toread)
