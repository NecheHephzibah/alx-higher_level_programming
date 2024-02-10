#!/usr/bin/python3
"""Represents a function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """defines a function that converts python object to JSON string"""

    return json.dumps(my_obj)
