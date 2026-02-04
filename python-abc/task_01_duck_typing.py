#!/usr/bin/env python3
"""Task 01: Duck Typing Example"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class implementing the Shape abstract base class."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self.radius**2 * pi)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return (2 * pi * self.radius)

class Rectangle(Shape):
    """Rectangle class implementing the Shape abstract base class."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return (self.height * self.width)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return (2 * (self.height + self.width))


def shape_info(shape):
    """Function that takes a shape object and prints its area and perimeter."""

    print('Area: {}'.format(shape.area()))
    print('Perimeter: {}'.format(shape.perimeter()))
