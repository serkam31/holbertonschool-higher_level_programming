#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i + (i >= 101) + (i >= 113))), end="")
