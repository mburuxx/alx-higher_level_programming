#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))

    sum = 0
    for i in range(len(unique_list)):
        sum += unique_list[i]

    return sum
