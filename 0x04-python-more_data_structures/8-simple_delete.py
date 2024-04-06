#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

    Args:
        a_dictionary: a dict object
        key: a string to be deleted

    Returns:
        a_dictionary: dictionary with deleted key
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
