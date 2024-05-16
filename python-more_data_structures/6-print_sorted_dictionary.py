#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    mix = sorted(a_dictionary.keys())
    for i in mix:
        print(f"{i}: {a_dictionary[i]}", end="\n")
