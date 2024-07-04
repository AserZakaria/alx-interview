#!/usr/bin/python3
"""
Solution to lockboxes problem
"""
def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """

    n = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    return len(opened_boxes) == n
