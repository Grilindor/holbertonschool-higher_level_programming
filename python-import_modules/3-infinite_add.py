#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    total = 0
    for i in range(1, argc):
        total += int(argv[i])
    print("{}".format(total))


# other possibility
# import sys
# def add_arguments(*args):
#    total = sum(int(arg) for arg in args)
#    print(total)
# if __name__ == "__main__":
#    add_arguments(*sys.argv[1:])
