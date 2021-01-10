#!/usr/bin/python3

"""Calculate sum of two integers
Args:
a: The first parameter
b: The second parameter
Returns: sum of 2 parameters"""


def add_integer(a, b=98):
    """
    Calculate sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
