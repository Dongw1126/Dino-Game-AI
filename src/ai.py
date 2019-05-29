import numpy as np

def ReLU(x):
    return np.maximum(0, x)

class Generation:
    def __init__(self):
        self.generation = 1
        self.enemy_pos = []
        self.runner_pos = []

    
