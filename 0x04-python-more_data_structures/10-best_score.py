#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
            return None
    max_score = 0
    key = None
    for k, v in a_dictionary.items():
        if v > max_score:
            max_score = v
            key = k
    return key
