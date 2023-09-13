#!/usr/bin/python3
"""This is responsible for defining a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """This Inserts text after each line containing a given string in a file.
    Args:
        filename (str):This is The name of the file.
        search_string (str):This is the The string to search for within the file.
        new_string (str):This is The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
