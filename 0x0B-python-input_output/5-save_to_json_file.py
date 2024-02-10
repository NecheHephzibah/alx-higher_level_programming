#!/usr/bin/python3

"""Represents a function that writes an Object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Defines the function conversion of Obj file to JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
