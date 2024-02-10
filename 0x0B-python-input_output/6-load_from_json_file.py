#!/usr/bin/python3

"""Represents a function that writes an Object to a text file using JSON"""
import json


def load_from_json_file(filename):
    """Defines the function conversion of Obj file to JSON representation"""
    with open(filename) as f:
        return json.load(f)
