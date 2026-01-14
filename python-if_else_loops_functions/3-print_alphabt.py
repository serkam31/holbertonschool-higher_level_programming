#!/usr/bin/python3
for i in range(97, 121):
    print("{}".format(chr(i + (i >= 101) + (i >= 112))), end="")
