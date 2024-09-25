#!/usr/bin/env python3

"""
This module defines an abstract base class `Shape` with abstract methods 
for calculating the area and perimeter. It also includes implementations 
of these methods for `Circle` and `Rectangle` shapes, and a utility 
function `shape_info` to display shape details.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    
    Methods:
        area(): Abstract method to compute the area of the shape.
        perimeter(): Abstract method to compute the perimeter of the shape.
    """
    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape."""
        pass

class Circle(Shape):
    """
    A class representing a circle, inheriting from the Shape class.
    
    Attributes:
        radius (float): The radius of the circle.
    
    Methods:
        area(): Returns the area of the circle.
        perimeter(): Returns the perimeter of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle (πr²)."""
        return self.radius**2 * 3.14
    
    def perimeter(self):
        """Returns the perimeter of the circle (2πr)."""
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from the Shape class.
    
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    
    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle (2 * (width + height))."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Displays information about a shape's area and perimeter.
    
    Args:
        shape (Shape): An instance of a class derived from `Shape`.
    
    Returns:
        str: A formatted string with the shape's area and perimeter.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    return f"Area: {area}, Perimeter: {perimeter}"
