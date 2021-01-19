#!/usr/bin/python3
""" Sorting a list """


class MyList(list):
    """ class """
    def print_sorted(self):
        """ function to sort order """
        new_list = self[:]
        new_list.sort()
        print(new_list)
