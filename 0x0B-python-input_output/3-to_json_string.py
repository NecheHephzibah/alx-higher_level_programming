#!/usr/bin/python3
import json
"""Represents a function that returns the JSON representation"""


def to_json_string(my_obj):
    """defines a function that converts python object to JSON string"""

    return json.dumps(my_obj)
