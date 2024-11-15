#!/usr/bin/python3
"""
Module 6-load_from_json_file
Defines a function that creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename (str): The name of the JSON file.
    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
