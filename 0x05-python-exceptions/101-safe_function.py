#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        if args:
            result = fct(*args)
        else:
            result = fct()
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
