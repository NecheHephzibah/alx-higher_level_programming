#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute_num = abs(number)
last_digit = absolute_num % 10
if last_digit > 5:
    condition = "and is greater than 5"
elif last_digit == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"

print(f"The Last digit of {number} is {last_digit} {condition}")
