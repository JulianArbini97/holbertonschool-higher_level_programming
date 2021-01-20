#!/usr/bin/python3
""" comment of the exercise """


def append_after(filename="", search_string="", new_string=""):
    """ func to append """
    with open(filename, 'r') as MyFile:
        lines = MyFile.readlines()

    with open(filename, 'w') as MyFile:
        for i in lines:
            if search_string in i:
                MyFile.write(i + new_string)
            else:
                MyFile.write(i)
