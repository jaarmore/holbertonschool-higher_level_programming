#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        sum_list = 0
        new_list = list(set(my_list))
        for elem in new_list:
            sum_list += elem
        return sum_list
