#!/usr/bin/python3
"""
This module defines a function `is_same_class` that checks
if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determines if `obj` is exactly an instance of `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if `obj` is exactly an instance of `a_class`.
        False otherwise.
    """
    return isinstance(obj, a_class)
