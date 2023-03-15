#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = [[matrix[i][j] ** 2 for i in range(n)] for j in range(m)]
    return new_matrix
