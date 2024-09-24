#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class.

The `BaseGeometry` class provides a foundation for geometry-related
operations, including an unimplemented `area` method and an
`integer_validator` method for validating integer values.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    Methods:
        area(self): Raises an exception, to be implemented in subclasses.
        integer_validator(self, name, value): Validates that a given value is
                                              a positive integer.
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

    def integer_validator(self, name, value):
        """
        Validates that the `value` is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The integer value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than 0.

        Example:
            integer_validator("width", 5)  # Valid input
            integer_validator("width", -2) # Raises ValueError
            integer_validator("width", "5") # Raises TypeError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
