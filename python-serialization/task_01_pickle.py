#!/usr/bin/python3
"""
A module for serializing and deserializing a custom Python object using pickle.
"""


import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize the class objects"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """Serialize the current instance of the object and save it to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file and return the instance."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Error deserializing object: {e}")
            return None
