#!/usr/bin/python3
"""Defines a JSON string-to-object function."""


def from_json_string(my_str):
    """Return the Python representation of a JSON string."""
    import json
    return json.loads(my_str)
