import numpy as np
import pygame as pg
import random
from game import Dino

RAND_INIT = 10

def rand():
    return random.uniform(-RAND_INIT, RAND_INIT)

def np_rand(arr, row ,col):
    for i in range(row):
        for j in range(col):
            arr[i][j] = rand()

def ReLU(x):
    return np.maximum(0, x)

class Instance:
    def __init__(self):
        self.dino = Dino(44,47)
        self.init_network()
        self.X = np.array([1.0, 1.0, 1.0, 1.0])

    def init_network(self):
        self.W1 = np.zeros((4, 3))
        self.W2 = np.zeros((3, 3))
        self.W3 = np.zeros((3 ,2))
        np_rand(self.W1, 4, 3)
        np_rand(self.W2, 3, 3)
        np_rand(self.W3, 3, 2)

        self.b1 = np.zeros((1, 3))
        self.b2 = np.zeros((1, 3))
        self.b3 = np.zeros((1, 2))
        np_rand(self.b1, 1, 3)
        np_rand(self.b2, 1, 3)
        np_rand(self.b3, 1, 2)

    def get_enemy_pos(self, cacti, ptreas):
        front_c = pg.Rect(600, 100, 40, 40)
        for c in cacti:
            if c.rect.x < front_c.x:
                front_c = c.rect

        front_p = pg.Rect(600, 100, 40, 40)
        for p in ptreas:
            if p.rect.x < front_p.x:
                front_p = p.rect
                
        self.X = np.array([front_c.x, front_c.y, front_p.x, front_p.y])
        

class Generation:
    def __init__(self, n):
        self.generation = 1
        self.num = n
        self.instance = []
    
    def create_instance(self):
        for i in range(num):
            self.instance.append(Instance())

    def generation_end(self):
        for i in range(num):
            if self.instance.isDead == False:
                return False
        return True
