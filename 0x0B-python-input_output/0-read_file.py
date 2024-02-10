#!/usr/bin/python3

"""This module contains a function that can open and read files."""

def read_file(filename=""):
    """Defines function that opens a file in read mode."""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line)
