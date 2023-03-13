#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_str = my_string.translate({ord(c) : None for c in "Cc"})
        return new_str
