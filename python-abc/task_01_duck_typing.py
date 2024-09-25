#!/usr/bin/env python3

"""
Defines an abstract Shape class with area and perimeter methods.
Includes Circle and Rectangle classes implementing these methods,
and a shape_info function to display their details.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

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
    Represents a circle shape.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return 3.14 * self.radius**2

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Displays the area and perimeter of a shape.

    Args:
        shape: An object with area and perimeter methods.
    """
    try:
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
    except AttributeError:
        print("The object does not have area or perimeter methods.")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(circle)
    print("\nRectangle Info:")
    shape_info(rectangle)
