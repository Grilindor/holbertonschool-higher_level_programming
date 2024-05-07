#!/usr/bin/python3

for i in range(ord('a'), ord('z')):
    if i == ord('e') or i == ord('q'):
        continue
    print("{:c}".format(i), end='')
