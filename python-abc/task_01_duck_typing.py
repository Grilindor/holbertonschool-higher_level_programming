#!/usr/bin/env python3

import math
from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * (math.pi * self.radius)

    def perimeter(self):
        return math.pi*(self.radius * 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Test cases
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)
    print()

    print("Rectangle info:")
    shape_info(rectangle)
