#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py). """


class BaseGeometry:
    """ what says up there """
    def area(self):
        """ area of the figure """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the number """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


""" Program that creates a Rectangle and intance its values """


class Rectangle(BaseGeometry):
    """ the inherit from BaseGeometry """
    def __init__(self, width, height):
        """ init function """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
