#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the student."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
