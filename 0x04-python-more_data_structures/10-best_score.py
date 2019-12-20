#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        greater = 0
        for key, value in a_dictionary.items():
            if value > greater:
                greater = value
                best = key
        return best
    return
