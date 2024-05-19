#!/usr/bin/python3

def no_c(my_string):
    cp_my_string = my_string.translate({ord(i): None for i in 'Cc'})
    return cp_my_string
