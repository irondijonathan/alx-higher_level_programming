#!/usr/bin/python3
"""This is for defining a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """This Return the JSON representation of a string object."""
    return json.dumps(my_obj)
