#!/usr/bin/python3
"""This is responsible for defining a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """This Creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
