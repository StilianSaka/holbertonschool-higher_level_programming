#!/usr/bin/python3
"""
Module for shapes with area and perimeter calculations.
"""


from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Defines the interface for calculating area and perimeter.
    """
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle shape class inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.141592653589793 * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): An instance of a class inheriting from Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
