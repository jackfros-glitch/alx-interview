#!/usr/bin/python3
'''
This script takes in a list of locked boxes with the first 
box opened by default and determines if the other boxes can
be unlocked by the keys by the keys available in the boxes

This file can also be imported as a module and contains only one function
which is:
 *canUnlockAll -> takes in a list of locked boxes which contains
    keys that may or may not be able to open all the boxes in the list 
    the function returns True if the keys available in the boxes can
    open all the boxes in the list of boxes and false if the avaible keys 
    cannot 
'''

def canUnlockAll(boxes: list) -> bool:
    '''
    takes in a list of boxes and determine if the keys in the boxes
    can open all the boxes available in the list

    Parameters
    ---------
    boxes : list

    Returns
    --------
    a boolean True or False

    '''
    if boxes == []:
        return False

    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys:
                keys.append(key)
    return True if len(keys) == len(boxes) else False
