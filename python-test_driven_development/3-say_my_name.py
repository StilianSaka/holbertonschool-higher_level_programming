#!/usr/bin/python3
# The shebang line specifies the script interpreter to use: Python 3.
def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the full name.

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    TypeError: If `first_name` or `last_name` is not a string.

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
