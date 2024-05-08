#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        tree = i % 3
        five = i % 5
        if tree == 0 and five == 0:
            print("FizzBuzz ", end="")
        elif five == 0:
            print("Buzz ", end="")
        elif tree == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(int(i)), end="")
