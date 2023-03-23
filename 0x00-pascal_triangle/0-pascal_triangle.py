#!/usr/bin/python3
"""
A python module for working with pascals triangle
"""
def pascal_triangle(n):
    """
    a method that returns a list of list of pascal triangle
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or i == j:
                row.append(1)
            elif j > 0 and i > 0:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle