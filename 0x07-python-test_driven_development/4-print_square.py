#!/usr/bin/python3

"""Print fill the square (size x size) wil "#"
Args:
size: size of square
Returns: nothing"""


def print_square(size):
    """print square of "#" by a given size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
