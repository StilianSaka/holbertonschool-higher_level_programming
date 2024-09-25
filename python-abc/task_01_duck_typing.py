#!/usr/bin/env python3

"""
This module demonstrates the use of abstract base classes (ABCs) and 
duck typing in Python with shapes such as Circle and Rectangle.

The Shape class serves as an abstract base class with area and perimeter 
methods, while Circle and Rectangle provide concrete implementations of 
these methods.

The shape_info function accepts any object that has area and perimeter 
methods and displays the results, showcasing the concept of duck typing.
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
        return 3.14 * self.radius**2

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
    def __init__(self, width, height):
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
        shape: An instance of a class that implements area and perimeter methods.
    
    Prints:
        The area and perimeter of the shape.
    """
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print(f"Area: {area}, Perimeter: {perimeter}")
    except AttributeError:
        print("The object does not have area or perimeter methods.")

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(circle)
    print("\nRectangle Info:")
    shape_info(rectangle)
