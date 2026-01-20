#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_list = sum(new_list)
    return sum_list
# return sum(set(my_list))