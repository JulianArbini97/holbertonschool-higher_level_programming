#!/usr/bin/python3

"""Calculate sum of two integers
Args:
a: The first parameter
b: The second parameter
Returns: sum of 2 parameters"""


def matrix_divided(matrix, div):
    """Check the matrix if its rows have same size
    and check element must be integer or float type
    """
    e1 = "Each row of the matrix must have the same size"
    e2 = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = list(map(list, matrix))
    large = 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        for col in row:
            if large == 0:
                large = len(row)
            elif large != len(row):
                raise TypeError(e1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(new_matrix[i][j]) is not int:
                if type(new_matrix[i][j]) is not float:
                    raise TypeError(e2)
            new_matrix[i][j] = round(matrix[i][j]/div, 2)
    return new_matrix
