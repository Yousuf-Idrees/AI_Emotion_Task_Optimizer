# algorithms.py

import random

# Judy
def csp_filter(tasks, emotion):
    return [t for t in tasks if emotion in t.emotion_fit]

# Marwan
def greedy(tasks):
    return max(tasks, key=lambda t: t.priority)

# Idrees
def hill_climbing(tasks, current):
    neighbors = [t for t in tasks if abs(t.priority - current.priority) <= 1]
    return max(neighbors, key=lambda t: t.priority, default=current)

# Mariam
def stochastic(tasks):
    weights = [t.priority for t in tasks]
    return random.choices(tasks, weights=weights)[0]

# Farida
def mini_a_star(tasks):
    # assign score first
    scored = [(t.priority + len(t.emotion_fit), t) for t in tasks]
    # sort by score
    scored.sort(key=lambda x: x[0], reverse=True)
    # return only Task objects
    return [t for score, t in scored[:2]]
