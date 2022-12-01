#!/usr/bin/python3
"""
This Script determines if a given data set represents a valid UTF-8 encoding.

This file can also be imported as a module and contains only one function
which is:
 *validUTF -> takes in a data set and then dataemines if it represents a 
    valid UTF-8 encoding the function returns True if the data set is a
    valid UTF-8 encoding 
"""


def validUTF8(data) -> bool:
    """
    takes in a data set and determines if the given data set represents a
    valid UTF-8 encoding.

    Parameters
    -----------
       data : list 

    :return:
       a boolean value True or False
       
    """
    num_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0