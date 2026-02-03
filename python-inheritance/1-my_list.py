#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list"""


class MyList(list):
    """Subclass of list that adds a method to print the list in sorted order"""

    def print_sorted(self):
        """Prints the list in sorted order"""
        print(sorted(self))
