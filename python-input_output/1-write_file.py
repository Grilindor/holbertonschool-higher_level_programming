#!/usr/bin/python3
"""
    function that writes a string to a text file and
    returns the numb of charac written
"""


def write_file(filename="", text=""):
    """returns the numb of charac written"""
    with open(filename, mode="w", encoding="utf-8") as file1_toread:
        file1_toread.write(text)
        return len(text)
