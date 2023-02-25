#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        a = 0
        for col in row:
            length = len(row)
            a += 1
            print('{:d}'.format(col), end='')
            if a != length:
                print(' ', end='')
        print('')
