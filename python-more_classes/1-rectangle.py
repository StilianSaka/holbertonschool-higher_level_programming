#!/usr/bin/python3
"""
This module defines a Rectangle class.

Classes:
    Rectangle: A class that defines a rectangle with width and height.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).

    Methods
    -------
    __init__(self, width=0, height=0):
        Initializes a new Rectangle instance with width and height.

    width(self):
        Getter for the width attribute.

    width(self, value):
        Setter for the width attribute. Validates that the value is an integer.

    height(self):
        Getter for the height attribute.

    height(self, value):
        Setter for the height attribute.Validates that the value is an integer.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with the provided width and height.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).

        Raises
        ------
        TypeError
            If the width or height is not an integer.
        ValueError
            If the width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns
        -------
        int
            The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle. Ensures the width is an integer.

        Parameters
        ----------
        value : int
            The new width of the rectangle.

        Raises
        ------
        TypeError
            If the width is not an integer.
        ValueError
            If the width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns
        -------
        int
            The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.Ensures the height is an integer

        Parameters
        ----------
        value : int
            The new height of the rectangle.

        Raises
        ------
        TypeError
            If the height is not an integer.
        ValueError
            If the height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
