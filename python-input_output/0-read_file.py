#!/usr/bin/python3
"""Module that contains the function read_file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")