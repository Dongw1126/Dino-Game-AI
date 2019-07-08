import numpy as np
import pygame as pg
import random
import math

REPLAY_MEMORY = 50000

def ReLU(x):
    return np.maximum(0, x)

def He_init(row, col):
    return np.random.randn(row, col)/np.sqrt(row)

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]
        
        x[i] = tmp + h
        f1 = f(x)

        x[i] = tmp - h
        f2 = f(x)

        grad[i] = (f1 - f2)/(2*h)

        x[i] = tmp

    return grad

def loss_function():
    pass

class Adam:

    """Adam (http://arxiv.org/abs/1412.6980v8)"""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None
        
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
        
        self.iter += 1
        lr_t  = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)         
        
        for key in params.keys():
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
            
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)
            
class DQN:
    def __init__(self):
        self.input = np.array([1.0, 1.0])

        self.init_network()

    def init_network(self):
        self.network = {}

        W1 = He_init(2, 3)
        W2 = He_init(3, 3)
        W3 = He_init(3, 3)

        b1 = np.zeros((1, 3))
        b1 = np.zeros((1, 3))
        b1 = np.zeros((1, 3))

        self.network['W1'] = W1
        self.network['W2'] = W2
        self.network['W2'] = W2

        self.network['b1'] = b1
        self.network['b2'] = b2
        self.network['b3'] = b3

    def predict(self):
        pass

    def update(self):
        pass

