#!/usr/bin/python3
"""
Class Square: creates a square class
"""


class Square:
    """create class"""
    def __init__(self, size=0):
        """initializes data"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates area"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
