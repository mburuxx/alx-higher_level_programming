#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a new list

    Args:
        my_list: initial list
        search: element to replace in the list
        replace: new element

    Return:
        new_list
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
