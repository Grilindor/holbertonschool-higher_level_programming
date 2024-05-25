#!/usr/bin/python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] from the list.")

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))


