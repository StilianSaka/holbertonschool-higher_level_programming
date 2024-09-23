#!/usr/bin/python3
"""
This module defines a function `inherits_from` that checks
if an object is an instance of a class that inherited (directly or indirectly)
from the specified class, but is not an instance of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Determines if `obj` is an instance of a class that inherited
    (directly or indirectly) from `a_class`, but not if `obj`
    is exactly an instance of `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if `obj` is an instance of a subclass of `a_class`, but not
        an instance of `a_class` itself.
        False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
