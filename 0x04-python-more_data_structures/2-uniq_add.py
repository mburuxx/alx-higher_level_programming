#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list(only one for each integer)

    Args:
        my_list: a list of integers

    Return:
        sum: sum of the unique integers
    """
    unique_list = list(set(my_list))

    sum = 0
    for i in range(len(unique_list)):
        sum += unique_list[i]

    return sum
