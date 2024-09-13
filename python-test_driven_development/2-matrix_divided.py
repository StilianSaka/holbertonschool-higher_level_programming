#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements 
of a matrix by a given divisor.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): A list of lists where each sublist
                                             represents a row in the matrix.
        div (int/float): The divisor used to divide the elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if the rows of the matrix are not of the same size.
                   If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with the elements divided by div, 
                       rounded to 2 decimal places.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    try:
        row_size = len(matrix[0])
    except TypeError:
        raise TypeError("object of type 'int' has no len()")
    
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(elem / div, 2) for elem in row] for row in matrix]
