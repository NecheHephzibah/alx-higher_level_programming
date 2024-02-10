#!/usr/bin/python3
"""Represents a function that converts the JSON representation"""
import json


def from_json_string(my_str):
    """defines a function that converts JSON object to python string"""

    return json.loads(my_str)
