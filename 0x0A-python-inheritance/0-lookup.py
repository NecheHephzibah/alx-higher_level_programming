#!/usr/bin/python3
"""Represents module containing a function that return available attribute"""


def lookup(obj):
	"""
	Defines a method that returns available attributes and
	methods of an object.

	Args:
		obj (class): passes in the object to be printd.

	Returns:
		list of attributes and methods of an object.
	"""

	return dir(obj)
