#!/usr/bin/python3
"""Module that contains the function to_json_string."""
import json


def from_json_string(my_str):
    """Returns the Python representation of an JSON"""
    return json.loads(my_str)
