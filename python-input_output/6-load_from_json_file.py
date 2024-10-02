#!/usr/bin/python3
"""Module that contains the function to_json_string."""
import json


def load_from_json_file(filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, 'r', encoding="uft-8") as f:
        obj = json.load(f)
    return obj
