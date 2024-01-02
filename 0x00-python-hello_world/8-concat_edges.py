#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + chr(32) + str[107:111] + chr(32) + chr(80) + chr(121) + chr(116) + chr(104) + chr(111) + chr(110)
print(str)
