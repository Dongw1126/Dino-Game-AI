import numpy as np
import pygame as pg
import random
import copy
import pickle
#from game import Dino

REPLAY_MEMORY = 50000

def ReLU(x):
    return np.maximum(0, x)

def Adam():
    pass

class DQN:
    def __init__(self):
        self.input = np.array([1.0, 1.0])

        self.init_network()

    def init_network(self):
        self.network = {}

        W1 = np.random.rand((2, 3))
        W2 = np.random.rand((3, 3))
        W3 = np.random.rand((3, 3))

        b1 = np.random.rand((1, 3))
        b2 = np.random.rand((1, 3))
        b3 = np.random.rand((1, 3))

        self.network['W1'] = W1
        self.network['W2'] = W2
        self.network['W2'] = W2

        self.network['b1'] = b1
        self.network['b2'] = b2
        self.network['b3'] = b3

    def predict(self):
        pass
        
