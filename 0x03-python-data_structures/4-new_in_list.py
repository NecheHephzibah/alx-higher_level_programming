#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nlist = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return nlist
    nlist[idx] = element
    return nlist
