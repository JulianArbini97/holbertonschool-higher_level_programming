#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return (None)
        if (idx == i):
            new_list = my_list.copy()
            new_list[idx] = element
            return (new_list)