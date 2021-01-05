#!/usr/bin/python3
"""
Class Square: Defines a square
"""


class Square:
    """ class square """
    def __init__(self, size=0):
        """ Initialize attributes"""
        self.size = size

    @property:
    def size(self):
        """ Initialize attributes"""
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
        """ sets the size with safe Assignment"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.size > 0:
            for a in range(self.size):
                for b in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
