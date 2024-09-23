#!/usr/bin/python3
"""
This module defines the function `lookup` that returns a list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to retrieve attributes and methods from.

    Returns:
        A list of strings representing the attributes and methods.
    """
    return dir(obj)
