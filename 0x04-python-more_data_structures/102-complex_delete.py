#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dup_dictionary = a_dictionary.copy()
    for i, j in dup_dictionary.items():
        if value == j:
            a_dictionary.pop(i)
    return a_dictionary
