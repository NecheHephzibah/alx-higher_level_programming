#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    i = chr(i)
    if i != 'q' and i != 'e':
        print("{}".format(i), end="")
