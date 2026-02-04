#!/usr/bin/python3
"""Module BaseGeometry: defines a base class for geometric shapes
with area calculation and integer validation methods.
"""


class BaseGeometry:
    """BaseGeometry class: provides area() that must be implemented
    by subclasses and integer_validator() to check positive integers.
    """

    def area(self):
        """Raises an Exception as area() is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable, used in error messages.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an int or is a bool.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
