#!/usr/bin/env python3
"""
Convert CSV data to JSON format.

This script reads data from a CSV file,
converts it to JSON format, and writes the JSON data to `data.json`.

Usage:
    $ python3 task_02_csv.py

Ensure that `data.csv` is in the same directory.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV to JSON.

    Args:
        csv_filename (str): The name of the CSV file.

    Returns:
        bool: True if successful, False if file not found.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
