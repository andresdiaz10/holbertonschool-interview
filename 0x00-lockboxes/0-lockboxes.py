#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    unlock_key = [0]

    for id, u_box in enumerate(boxes):
        for key in u_box:
            if key not in unlock_key and key != id and key < len(boxes):
                unlock_key.append(key)
    if len(boxes) == len(unlock_key):
        return True
    else:
        return False
    