#!/usr/bin/env python3

"""
This module defines an abstract base class `Animal` with an abstract method `sound`.
It also provides concrete implementations of this method in the subclasses `Dog` and `Cat`.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    
    Methods:
        sound(): Abstract method that should be overridden by subclasses 
                 to define the specific sound an animal makes.
    """
    @abstractmethod
    def sound(self):
        """Method to be implemented by subclasses to return the sound of the animal."""
        pass

class Dog(Animal):
    """
    A class representing a dog, inheriting from the Animal class.
    
    Methods:
        sound(): Returns the sound a dog makes ("Bark").
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    A class representing a cat, inheriting from the Animal class.
    
    Methods:
        sound(): Returns the sound a cat makes ("Meow").
    """
    def sound(self):
        return "Meow"
