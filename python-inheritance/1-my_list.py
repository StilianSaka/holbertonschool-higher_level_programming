#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from `list`
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in `list` class that adds a method to
    print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.

        The method uses the built-in `sorted()` function, which returns
        a new sorted list without modifying the original list.
        """
        print(sorted(self))
