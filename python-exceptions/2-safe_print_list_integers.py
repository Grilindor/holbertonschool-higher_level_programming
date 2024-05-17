#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            pass  # Continue to the next item if an error occurs
        if count == x:  # Check if desired number of integers have been printed
            break
    print()
    return count
