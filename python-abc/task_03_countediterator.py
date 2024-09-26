#!/usr/bin/env python3
"""
CountedIterator extends the built-in iterator to count items iterated.
"""


class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current count of iterated items."""
        return self.count

if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
