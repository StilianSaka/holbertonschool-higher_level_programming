#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load data from a file and deserialize it."""
    with open(filename, 'r') as file:
        return json.load(file)
