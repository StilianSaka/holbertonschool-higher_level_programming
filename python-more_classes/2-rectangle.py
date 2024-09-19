#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).

    Methods:
        __init__(self, width=0, height=0): Initializes a Rectangle instance.
        width(self): Getter for the width attribute.
        width(self, value): Setter for the width attribute.
        height(self): Getter for the height attribute.
        height(self, value): Setter for the height attribute.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with width and height.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width. Validates the input.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height. Validates the input.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
