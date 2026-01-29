#!/usr/bin/python3
"""Module that defines a Square class with size validation"""


class Square:
    """Class that represents a square defined by its size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square instance.
        size: size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.position = position

    def area(self):
        """Calculate and return the area of the square.
           Returns: the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character.
            Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)

    @property
    def size(self):
        """Getter for the size attribute.
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation.
            Args:
            value (int): New size of the square.
            Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute.
            int: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute with validation.
            Args:
            value (int): New size of the square.
            Raises:
            TypeError: If value is not an integer.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value