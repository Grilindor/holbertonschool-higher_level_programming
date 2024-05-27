#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creates an Object and return it"""
    with open(filename, "r", encoding='utf-8') as file6_toread:
        return json.load(file6_toread)
