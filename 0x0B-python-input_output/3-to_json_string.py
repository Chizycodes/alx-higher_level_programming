#!/usr/bin/python3
"""Defines a JSON string-to-object function."""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    import json
    return json.dumps(my_obj)
