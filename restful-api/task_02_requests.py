#!/usr/bin/python3

"""
Script: Fetch and Save Posts

Description:
Fetches posts from a public API, prints titles, and saves posts to a CSV file.

Dependencies:
- requests: HTTP library for Python.
- csv: Module for handling CSV files.

Functions:
- fetch_and_print_posts(): Prints post titles.
- fetch_and_save_posts(): Saves posts to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetches posts and prints titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")  # Print the status code
    if response.status_code == 200:
        for post in response.json():
            print(post['title'])


def fetch_and_save_posts():
    """Fetches posts and saves them to a CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        with open('posts.csv', 'w', newline='') as file:
            fieldnames = ['id', 'title', 'body']  # Exclude 'userId'
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in response.json():
                # Remove 'userId' from each post
                post.pop('userId', None)
                writer.writerow(post)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
