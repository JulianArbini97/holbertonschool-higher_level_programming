#!/usr/bin/python3

"""Print a paragraph
Args:
size: size of square
Returns: nothing"""


def text_indentation(text):
    """print paragraph and give space after ".?:"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    period = text.replace('. ', '.\n\n')
    period1 = period.replace('? ', '?\n\n')
    period2 = period.replace(': ', ':\n\n')
    print(period2, end='')
