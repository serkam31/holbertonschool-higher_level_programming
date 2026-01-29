#!/usr/bin/python3
"""Module that defines a Square class with size validation"""


class Square:
    """Class that represents a square defined by its size"""
    def __init__(self, size=0):
        """Initialize a new square instance.
        size: size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculate and return the area of the square.
           Returns: the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
