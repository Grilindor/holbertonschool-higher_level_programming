#!/usr/bin/env python3
"""
    module that adds serialize a Python dictionary to a JSON file and
    deserialize the JSON file to recreate the Python Dictionary
"""


import json


def serialize_and_save_to_file(data, filename):
    """save Python Dictionary in JSON file"""
    with open(filename, mode="w") as file1_toread:
        json.dump(data, file1_toread)


def load_and_deserialize(filename):
    """deseialized JSON file to Python Dictionary"""
    with open(filename, "r", encoding='utf-8') as file6_toread:
        return json.load(file6_toread)
