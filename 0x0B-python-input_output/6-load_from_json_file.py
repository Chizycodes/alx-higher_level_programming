#!/usr/bin/python3
"""Defines a JSON string-to-object function."""
import json


def load_from_json_file(filename):
    """Create an Object from a “JSON file”."""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
