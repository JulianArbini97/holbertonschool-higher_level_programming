#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py). """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """
    def __init__(self, size):
        """ init """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """area of the square """
        return (self.__size ** 2)
