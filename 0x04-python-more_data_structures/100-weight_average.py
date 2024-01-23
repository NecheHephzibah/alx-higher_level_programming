#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    i = 0

    for tupple in my_list:
        number = number + tupple[0] * tupple[1]
        i = i + tupple[1]

    return (number / i)
