"""
Hill-Climbing Algorithm in 3D Search Space
    - Greepy Approach
    - Simple Hill-Climbing

1. Evaluate initial state to see if it is the goal state
    - Goal State: Gradient doesn't change or bound is reached
    - If not, make initial state the current state
2. Loop until solution state are reached or resources are exhausted
    a. Select a non-discovered state 
    b. Evaluate new state
        i. If goal, stop
        ii. if better, make current and continue
        iii. If not better, continue loop auntil solution is found
"""

import numpy as np
import random
import matplotlib.pyplot as plt


def hill_climb_3D(node):
    grad = 0
    for i in range(1000):
        if sum(node) <= -10:
            return [-5, -5]
        elif sum(node) >= 10:
            return [5, 5]
        else:   
            center = node[0]**4 - 22 * (node[0]**2) + node[1]**4 - 22 * (node[1]**2)
            left = np.subtract(node, (random.random(), random.random()))
            left_y = left[0]**4 - 22 * (left[0]**2) + left[1]**4 - 22 * (left[1]**2)
            right = np.add(node, (random.random(), random.random()))
            right_y = right[0]**4 - 22 * (right[0]**2) + right[1]**4 - 22 * (right[1]**2)
            if left_y >= right_y:
                if left_y > center:
                    node = left
            elif left_y < right_y:
                if right_y > center:
                    node = right
    return node