#!/usr/bin/python3
"""
This model provides  function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description
    with simple data structure for
    JSON serialization of an object.
    """
    return obj.__dict__
