#!/usr/bin/python3

def uppercase(str):
    for i in str:
        up = 0
        if ord(i) >= 97 and ord(i) <= 122:
            up = ord(i) - 32
        else:
            up = ord(i)
        print("{}".format(chr(up)), end="")
    print("")
    return
