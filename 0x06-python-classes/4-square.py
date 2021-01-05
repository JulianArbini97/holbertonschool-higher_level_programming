#!/usr/bin/python3
"""
Class Square: Defines a square
"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """ Initialize attributes"""
        self.size = size

    @property:
    def size(self):
        """ gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with safe Assignment"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__value = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size ** 2)
