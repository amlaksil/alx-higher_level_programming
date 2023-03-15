#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[matrix[j][i] ** 2 for i in range(m)] for j in range(n)]
    return new_matrix
