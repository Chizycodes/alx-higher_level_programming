#!/usr/bin/python3
for letter in range(97, 123):
    if (not chr(letter) == "q") and (not chr(letter) == "e"):
        print("{}".format(chr(letter)), end="")
