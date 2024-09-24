#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class.

The `BaseGeometry` class serves as a foundation for geometry-related
operations and enforces that subclasses must implement the `area` method.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
        area(self): Raises an exception, to be implemented in subclasses.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        This method is intended to be overridden in subclasses that provide
        a specific area calculation for different geometric shapes.

        Raises:
            Exception: Always raises this exception to signal that the method
            must be implemented in any subclass.
        """
        raise Exception("area() is not implemented")
