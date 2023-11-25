#!/usr/bin/python3

def canUnlockAll(boxes):
        n = len(boxes)
        keys = [0]  # Start with the key to the first box
        visited = set(keys)

        while keys:
                        current_box = keys.pop()
                        for key in boxes[current_box]:
                            if key < n and key not in visited:
                                                                            keys.append(key)
                                                                            visited.add(key)

        return len(visited) == n
