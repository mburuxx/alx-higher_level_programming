#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square values of all elements in the matrix

    Args:
        matrix: 2d array

    Return:
        new matrix: each value is the square of all input values
    """
    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x**2, matrix[i])))

    return new_matrix
