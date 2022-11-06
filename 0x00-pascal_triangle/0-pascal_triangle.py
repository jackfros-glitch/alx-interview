#!/usr/bin/python3

'''
This script allows the user to genrate a list of lists of integers representing the Pascal’s triangle of n
n -> the number of rows the users wants to generate
This file can also be imported as a module and contains only one function
which is:
 * pascal_traingle -> takes in the number of rows in the pascal's Triangle to be generated and
        returns a list of lists of integers representing the Pascal’s triangle
'''


def pascal_triangle(n):
    ''' takes in the number of rows in the pascal's Triangle that the user wants to generate

    Parameters
    -----------
    n : integer
        The number of rows to be generated

    Returns
    ------------
    res : list
        a list of lists of integers representing the Pascal’s triangle
    '''
    res = [[1]]
    for i in range(n - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        res.append(row)
    return res
