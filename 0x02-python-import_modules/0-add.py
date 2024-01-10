#!/usr/bin/python3
my_import = getattr(__import__('add_0'), 'add')
a = 1
b = 2
result = my_import(a, b)
print("{} + {} = {}".format(a, b, result))
