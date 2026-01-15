#!/usr/bin/python3
def uppercase(str):
    string = ""
    for c in str:
        if 'a' < c < 'z':
            string += chr(ord(c) - 32)
        else:
            string += c
    print("{:s}".format(string), end="")
    print()
