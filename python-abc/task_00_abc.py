#!/usr/bin/env python3
"""Task 00: Abstract Base Class Example"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Method to be implemented by subclasses
           to return the sound of the animal.
        """
        pass


class Dog(Animal):
    """Dog class implementing the Animal abstract base class."""
    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing the Animal abstract base class."""
    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"
