#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 1:
        print('1 argument:')
    elif argc == 0:
        print('0 arguments.')
    else:
        print('{:d} arguments:'.format(argc))

    for arguments in range(1, argc + 1):
        print('{:d}: {}'.format(arguments, sys.argv[arguments]))
