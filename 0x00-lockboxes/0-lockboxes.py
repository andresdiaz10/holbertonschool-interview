#!/usr/bin/python3
def canUnlockAll(boxes):
    none_Counter = 0
    key_Counter = 0
    size = len(boxes) - 1
    for l in boxes:
        if not l:
            none_Counter += 1
        else:
            key_Counter += 1
    if not boxes[size] and none_Counter == 1:
        return True
    elif key_Counter > 0 and none_Counter == 0:
        return True
    else:
        return False
