#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0")
    elif length > 2:
        result = 0
        for i in range(1, length):
            result += int(sys.argv[i])
        print("{}".format(result))
