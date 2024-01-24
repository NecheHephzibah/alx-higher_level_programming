#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False



#if isinstance(value, int) and (value >= 0
#                      and value <= 9 or value < 0):
#           print("{:d}".format(value))
#           return True
#       else:
#           return False
#    except TypeError as exc:
#       print("{}".format(exc))
#       return False
