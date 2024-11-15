#!/usr/bin/python3
"""
Module 8-class_to_json
Defines a function that returns the dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON.
    Args:
        obj: The object to serialize.
    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
