#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unigue integers in a list (once for each integer)."""
    return sum(set(my_list))
    