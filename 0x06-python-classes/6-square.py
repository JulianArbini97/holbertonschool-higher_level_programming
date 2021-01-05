#!/usr/bin/python3
"""
Class Square: creates a square class
"""


class Square:
    """create class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates area"""
        return self.__size * self.__size

    def my_print(self):
        """print square with coordinates"""
        if self.__size == 0:
            print()
        if self.position:
            if self.__size > 0:
                print("\n" * self.__position[1], end="")
                for a in range(self.size):
                    print(" " * self.__position[0], end="")
                    print("#" * self.__size)
