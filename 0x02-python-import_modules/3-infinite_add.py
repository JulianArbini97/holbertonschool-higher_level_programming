#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    res = 0
    if argc != 0:
        for i in range(1, argc + 1):
            res = res + int(sys.argv[i])
    print('{:d}'.format(res))
