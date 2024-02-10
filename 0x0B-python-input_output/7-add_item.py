#!/usr/bin/python3
"""Represents a script that adds all arguments to a python."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-\
save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-\
load_from_json_file').load_from_json_file

    try:
        add_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        add_items = []
    add_items.extend(sys.argv[1:])
    save_to_json_file(add_items, "add_item.json")
