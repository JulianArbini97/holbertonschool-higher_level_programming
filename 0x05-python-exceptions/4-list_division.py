#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            new_list += [my_list_1[i] / my_list_2[i]]
        except(ZeroDivisionError):
            print("division by 0")
            new_list += [0]
            pass
        except(TypeError):
            print("wrong type")
            new_list += [0]
            pass
        except(IndexError):
            print("out of range")
            new_list += [0]
            pass
        finally:
            i += 1
    return new_list
