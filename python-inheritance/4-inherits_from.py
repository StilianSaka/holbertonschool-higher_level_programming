#!/usr/bin/python3
"""
Check if an object is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Determine if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass of a_class, else False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
