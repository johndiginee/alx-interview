#!/usr/bin/python3
"""Lockboxes."""


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    canUnlockAll = False
    keys = {0: True}
    Nboxes = len(boxes)
    while (True):

        Nkeys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < Nboxes:
                        keys[j] = True
                    boxes[i] = None

        if not (len(keys) > Nkeys):
            break

    if Nkeys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
