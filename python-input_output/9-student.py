#!/usr/bin/python3
class Student:
    """A class representing a student with first name, last name, and age."""


    def __init__(self, first_name, last_name, age):
        """Initalization of the class objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
