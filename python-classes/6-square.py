#!/usr/bin/python3
"""
This module defines a `Square` class.

Classes:
    Square

Exceptions:
    TypeError
    ValueError
"""


class Square:
    """
    A class used to represent a Square

    ...

    Attributes
    ----------
    size : int
        the size of the square's side (default is 0)
    position : tuple
        the position of the square (default is (0, 0))

    Methods
    -------
    area():
        Returns the area of the square.
    my_print():
        Prints the square with the character #.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int, optional
            The size of the square's side (default is 0)
        position : tuple, optional
            The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters
        ----------
        value : int
            The size of the square's side

        Raises
        ------
        TypeError
            If size is not an integer
        ValueError
            If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters
        ----------
        value : tuple
            The position of the square

        Raises
        ------
        TypeError
            If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print("")
            return
        for y in range(self.position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
