#!/usr/bin/env python3
def uppercase(str):
    for s in range(len(str)):
        i = ord(str[s])
        if (i >= 97 and i <= 122):
            i = i - 32
        print("{}".format(chr(i)), end="")
    print()
