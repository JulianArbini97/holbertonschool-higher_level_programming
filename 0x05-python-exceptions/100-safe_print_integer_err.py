#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as exception:
        error = "Exception: " + str(exception) + "\n"
        sys.stderr.write(error)
        return False
