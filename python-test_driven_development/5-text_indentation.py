#!/usr/bin/python3
"""
This module provides a function `text_indentation` that prints a text with
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If the input text is not a string.

    Example:
        text_indentation("Hello. How are you? I am fine: thank you.")
        Output:
        Hello.

        How are you?

        I am fine:

        thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
