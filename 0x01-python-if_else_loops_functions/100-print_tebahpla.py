#!/usr/bin/python3
for n in range(122, 96, -1):
    if ((n % 2) != 0):
        n = n - 32
    print("{}".format(chr(n)), end="")
