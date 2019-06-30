import numpy as np
import pygame as pg
import random
import copy
import pickle
from game import Dino

REPLAY_MEMORY = 50000

def rand():
    return random.uniform(-RAND_INIT, RAND_INIT)

def np_rand(arr, row ,col):
    for i in range(row):
        for j in range(col):
            arr[i][j] = rand()

def ReLU(x):
    return np.maximum(0, x)

def Adam():
    pass

class DQN:
    def __init__(self):
        pass

    def init_network(self):
        pass

    def predict(self):
        pass
    
            
            
        
