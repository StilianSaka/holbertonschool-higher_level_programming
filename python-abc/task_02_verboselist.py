#!/usr/bin/env python3
"""
VerboseList prints notifications for list operations.
"""


class VerboseList(list):
    """A list that prints notifications for append, extend, remove, and pop."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove an item and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
