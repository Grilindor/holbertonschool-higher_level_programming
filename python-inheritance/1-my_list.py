#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Public instance method that prints the list, but sorted"""
<<<<<<< HEAD

=======
>>>>>>> 286d024e6282b3356b7ce307ed203e5d36e8e9fc
    def print_sorted(self):
        for append in self:
            if not isinstance(append, int):
                raise TypeError("not all elements in it are integer")
        print(sorted(self))
