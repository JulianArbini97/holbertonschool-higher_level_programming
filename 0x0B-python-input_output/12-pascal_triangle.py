#!/usr/bin/python3
'''Pascal triangle function'''


def pascal_triangle(n):
    '''
    Returns a list of lists
    with the pascal triangle
    '''
    r_list = []
    if n <= 0:
        return r_list
    a_list = []
    for line in range(0, n):
        a_list = []
        for i in range(0, line + 1):
            res = 1
            k = i
            j = line
            if (k > j - k):
                k = j - k
            for l in range(0, k):
                res = res * (j - l)
                res = res // (l + 1)
            a_list.append(res)
        r_list.append(list(a_list))
    return r_list
