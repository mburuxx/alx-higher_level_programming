#!/usr/bin/python3
def uppercase(str):
    """ Print a string in uppercase """
    for c in str:
        lower = ord(c)
        if (lower >= 97) and (lower <= 122):
            lower -= 32
        print("{}".format(chr(lower)), end="")
    print()
