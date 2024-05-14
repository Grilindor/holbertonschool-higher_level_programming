#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    yes_no_list = []
    for num in my_list:
        if num % 2 == 0:
            yes_no_list.append(True)
        else:
            yes_no_list.append(False)
    return yes_no_list

