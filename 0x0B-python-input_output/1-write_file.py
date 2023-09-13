#!/usr/bin/python3
"""This is a file-writing function."""


def write_file(filename="", text=""):
    """This Write a string to a UTF8 text file.
    Args:
        filename (str):This is The name of the file to write.
        text (str):This is the The text to write to the file.
    Returns:
        This is The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
