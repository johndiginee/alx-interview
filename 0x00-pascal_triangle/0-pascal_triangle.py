#!/usr/bin/python3
"""An ALX-Holberton School interview question on Pascal's Triangle."""


def pascal_triangle(n):
    """Function returns a list of lists of int representing the Pascal’s triangle of n
    Args:
        n (n): size of triangle
    Returns:
        list: returns empty list if n <= 0 or list of lists of int
        representing Pascal's triangle of n otherwise
    """
    if n <= 0:
        return []

    triangle, bufferList = [], []
    for x in range(n):
        if x == 0:
            triangle.append([1])
            continue
        if x == 1:
            triangle.append([1, 1])
            continue

        sumList = triangle[-1]
        for i in range(len(sumList) + 1):
            if i in [0, len(sumList)]:
                bufferList.append(1)
                continue
            bufferList.append(sumList[i] + sumList[i - 1])

        triangle.append(bufferList)
        bufferList = []

    return triangle
