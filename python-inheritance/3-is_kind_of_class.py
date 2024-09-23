#!/usr/bin/python3
"""
This module defines a function `is_kind_of_class` that checks
if an object is an instance of, or if the object is an instance
of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if `obj` is an instance of `a_class` or an instance
    of a class that inherited from `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if `obj` is an instance of `a_class` or a subclass of it.
        False otherwise.
    """
    return isinstance(obj, a_class)
