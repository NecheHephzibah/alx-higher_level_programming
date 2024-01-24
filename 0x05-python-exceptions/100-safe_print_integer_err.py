#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        if value is None:
            raise TypeError("NoneType is not an integer")
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
