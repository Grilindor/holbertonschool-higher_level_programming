#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dictionary = {}
    for key, value in a_dictionary.items():
        b_dictionary[key] = value * 2
    return b_dictionary
