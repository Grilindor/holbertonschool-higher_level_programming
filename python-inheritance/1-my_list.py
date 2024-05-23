#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        for append in self:
            if not isinstance(append, int):
                raise TypeError("not all elements in it are integer")
        print(sorted(self))

