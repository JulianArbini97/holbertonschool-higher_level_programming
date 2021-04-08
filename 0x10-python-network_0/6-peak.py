#!/usr/bin/python3
""" Test function find_peak """


def find_peak(integer_list):
    """ Finding the peak of a list """
    """ Board cases """
    # middle_point = len(integer_list)/2
    # print (middle_point)

    if len(integer_list) == 0:
        return None
    elif len(integer_list) == 1:
        return integer_list[0]
    elif len(integer_list) == 2:
        return max(integer_list)

    if len(integer_list) % 2 == 0:
        middle_point = int(len(integer_list)/2)
    else:
        middle_point = int((len(integer_list) - 1)/2)

    # print("PUNTO MEDIO: {}".format(middle_point))
    middle = integer_list[middle_point]
    next_int = integer_list[middle_point + 1]
    prev_int = integer_list[middle_point - 1]
    first_half = integer_list[:middle_point]
    # print("PRIMERA MITAD {}".format(first_half))
    second_half = integer_list[middle_point + 1:]
    print("SEGUNDA MITAD {}".format(second_half))

    if middle > prev_int and middle > next_int:
        return middle
    elif middle < prev_int and middle > next_int:
        return find_peak(first_half)
    else:
        return find_peak(second_half)
