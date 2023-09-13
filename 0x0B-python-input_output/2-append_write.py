#!/usr/bin/python3
"""This is a file-appending function."""


def append_write(filename="", text=""):
    """This Appends a string to the end of a UTF8 text file.
    Args:
        filename (str):This is the The name of the file to append to.
        text (str):This is The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
