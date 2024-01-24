#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        if value is None:
            raise TypeError("NoneType is not an integer")
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except ValueError:
        print("Exception: Cannot format float as integer",
              file=sys.stderr)
        return False
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
