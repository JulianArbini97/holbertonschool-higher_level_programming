#!/usr/bin/python3
"""
Class Square: creates a square class
"""
import math


class MagicClass:
    """define class"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(self.radius) is not int and type(self.radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self, radius):
        """calculates circ"""
        return self.__radius * 2 * math.pi
