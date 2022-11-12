#!/usr/bin/python3
'''
'''

def canUnlockAll(boxes: list) -> bool:
    '''

    Parameters
    ---------
    boxes : list

    Returns
    --------
    a boolean True or False

    '''
    keys = [0]
    for i in keys:
        for key in boxes[i]:
            if key not in keys:
                keys.append(key)
    return True if len(keys) == len(boxes) else False
