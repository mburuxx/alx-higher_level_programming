#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a = tuple_a + (0, ) * (2 - len(tuple_a))
        tuple_b = tuple_b + (0, ) * (2 - len(tuple_b))
    result = ()
    for elem in range(2):
        result = result + (tuple_a[elem] + tuple_b[elem], )
    return result
