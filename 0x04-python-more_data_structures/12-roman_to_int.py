#!/usr/bin/python3
def to_subtract(list_num):
    subtract = 0
    max_list = max(list_num)

    for i in list_num:
        if max_list > i:
            subtract = subtract + i

    return (max_list - subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    keys_list = list(roman_numerals.keys())

    number = 0
    last_roman = 0
    list_num = [0]

    for char in roman_string:
        for rom_num in keys_list:
            if rom_num == char:
                if roman_numerals.get(char) <= last_roman:
                    number += to_subtract(list_num)
                    list_num = [roman_numerals.get(char)]
                else:
                    list_num.append(roman_numerals.get(char))

                last_roman = roman_numerals.get(char)

    number += to_subtract(list_num)

    return number
