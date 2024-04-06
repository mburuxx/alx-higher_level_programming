#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary

    Args:
        a_dictionary: dict object

    Return:
        nb_keys: number of keys
    """
    # obtain the keys in a list
    keys = list(a_dictionary)

    # get length of the list
    nb_keys = len(keys)

    return nb_keys
