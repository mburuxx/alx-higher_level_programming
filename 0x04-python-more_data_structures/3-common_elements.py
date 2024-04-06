#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a common set of elements in two sets

    Args:
        set_1: first set
        set_2: second set

    Return:
        c_set: a common set
    """
    c_set = set_1 & set_2
    return c_set
