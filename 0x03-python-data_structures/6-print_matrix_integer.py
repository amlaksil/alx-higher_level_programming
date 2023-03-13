#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        n = len(matrix[i])
        for j in range(n):
            print("{:d}{}".format(matrix[i][j], " " if j != n - 1
                                  else ""), end="")
        print()
