#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes a text file (UTF8) and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
