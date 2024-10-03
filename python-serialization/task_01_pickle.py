#!/usr/bin/python3
"""Module containing pickle module and CustomObject"""

import pickle


class CustomObject:
    """The CustomObject class"""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialization of instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Method to serialize the Object and write it to the file"""

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print("Error occurred:", e)

    @classmethod
    def deserialize(cls, filename):
        """Method to deserialize the Object from file"""
        import pickle

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print("Error occurred:", e)
            return None
