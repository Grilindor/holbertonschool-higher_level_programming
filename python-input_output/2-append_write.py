#!/usr/bin/python3
"""
    a function that appends a string at the end of a text file
    and returns the number of characters added
 """


def append_write(filename="", text=""):
    """returns the numb of charac added"""
    with open(filename, mode="a", encoding="utf-8") as file2_toread:
        return file2_toread.write(text)
