#!/usr/bin/python3
""" Write a class BaseGeometry (based on 6-base_geometry.py). """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" Program that creates a Rectangle and intance its values """


class Rectangle(BaseGeometry):
    """ the inherit from BaseGeometry """
    def __init__(self, width, height):
        """ init function """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
