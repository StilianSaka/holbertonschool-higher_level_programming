#!/usr/bin/python3
"""
This module defines a Square class.

Classes:
    Square: A class that defines a square by its size and can compute its area.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    __size : int
        The size of the square (private).

    Methods
    -------
    __init__(self, size=0):
        Initializes the square with a given size.
    size(self):
        Retrieves the size of the square.
    size(self, value):
        Sets the size of the square with validation.
    area(self):
        Computes the area of the square.
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0).

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns
        -------
        int
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Parameters
        ----------
        value : int
            The size of the square.

        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns
        -------
        int
            The area of the square.
        """
        return self.__size ** 2
