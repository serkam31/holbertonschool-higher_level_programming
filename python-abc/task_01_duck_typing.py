#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


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
        print("Area: {}".format(self.radius**2 * pi))

    def perimeter(self):
        print("Perimeter: {}".format(2 * pi * self.radius))


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area: {}".format(self.height * self.width))

    def perimeter(self):
        print("Perimeter: {}".format((self.width + self.height) * 2))


def shape_info(shape):
    shape.area()
    shape.perimeter()
