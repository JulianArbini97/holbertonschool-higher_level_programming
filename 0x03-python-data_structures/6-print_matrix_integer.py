#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        s = ""
        for j in i:
            print("{:s}{:d}".format(s, j), end='')
            s = " "
        print()
