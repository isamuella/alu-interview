#!/usr/bin/python3
"""
Calculating how many square units of water will be retained after it rains.
"""


def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    trapped = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        trapped += max(0, water_level - walls[i])

    return trapped
