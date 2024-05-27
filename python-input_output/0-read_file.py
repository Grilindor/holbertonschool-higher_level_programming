#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as file0_toread:
        print(file0_toread.read(), end="")
