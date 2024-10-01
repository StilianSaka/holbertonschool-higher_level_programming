#!/usr/bin/python3
"""Module that contains the function write_file."""


def write_file(filename="", text=""):
    """Writes a string to a text file(UTF8) and returns the number of chars."""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
