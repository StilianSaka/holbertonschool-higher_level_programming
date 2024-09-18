#!/usr/bin/python3
"""
This module defines a Square class.

Classes:
    Square: A class that defines a square by its size.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes
    ----------
    __size : int
        The size of the square (private).
    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of the square.
        """
        self.__size = size
