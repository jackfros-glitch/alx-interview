#!/usr/bin/python3
'''
This Script calculate the minimun number of operations required to
perform n amount of operations to result in n H characters in the file
the number of operation is been given by the user as an arguements

This file can also be imported as a module and contains only one function
which is:
 *minOperations -> takes in the number of H character that need to be
    replicated in the file and returns the fewest number of operations
    needed to result in exactly n H characters in the file.
'''


def minOperations(n: int) -> int:
    '''
    takes in an integer and then returns the fewesthe fewest number of
    operations needed to result in exactly n H characters in the file.

    Parameters
    ----------
    n -> is the number of times the H character is to be replicated

    Returns
    --------
        an integer which represents the fewest number of operations
        needed to result in exactly n H characters in the file.

    '''
    if n <= 1:
        return 0
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
