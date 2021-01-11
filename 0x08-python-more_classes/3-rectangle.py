#!/usr/bin/python3
"""
Class Rectangle: Defines a Rectangle
"""


class Rectangle:
    """ class that defines a Rectangle with attributes and public methods"""
    def __init__(self, width=0, height=0):
        """ Initializes instances """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set passed private attribue of width """
        if type(value) is not int and type(value) is not float:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        if type(value) is not int and type(value) is not float:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ magic method that print the rectangle with the character # """
        result = ""

        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result = result + "#"
                result = result + '\n'
            result = result[:-1]
            return result
