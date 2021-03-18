"""
Hill-Climbing Algorithm in 2D Search Space
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


def hill_climb(node):
    grad = 0
    for i in range(1000):
        if node <= -5:
            return -5
        elif node >= 5:
            return 5
        else:   
            center = pow(node, 4) - 22*pow(node, 2) 
            left = node - random.random()
            left_y = left**4 - 22*(left**2)
            right = node + random.random()
            right_y = right**4 - 22*(right**2)
            if left_y >= right_y:
                if left_y > center:
                    node = left
            elif left_y < right_y:
                if right_y > center:
                    node = right
    return node