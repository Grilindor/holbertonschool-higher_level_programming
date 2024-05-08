#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    if argc - 1 == 0:
        print("{} argument.".format(argc - 1))
    elif argc == 2:
        print("{} arguments.".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
