#!/usr/bin/python3
"""
File: 0-rotate_2d_matrix.py - A python module for carrying
out a 90 degree rotation on n * n matrix
Author: kaleab shiferaw girma
Date: 11th may, 2023
"""


def rotate_2d_matrix(matrix):
    """
    A python method for carrying out the rotation
    Args:
        matrix -> int: is a number to show n * n where matrix == n
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
