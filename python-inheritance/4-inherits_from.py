#!/usr/bin/python3
"""Function that checks if an object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
