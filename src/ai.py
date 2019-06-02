import numpy as np
import pygame as pg
import random
from game import Dino

RAND_INIT = 5

def max_index(arr):
    v = np.argmax(arr)
    return v
        

def rand():
    return random.uniform(-RAND_INIT, RAND_INIT)

def np_rand(arr, row ,col):
    for i in range(row):
        for j in range(col):
            arr[i][j] = rand()

def ReLU(x):
    return np.maximum(0, x)

def identity_function(x):
    return x

class Instance:
    def __init__(self):
        self.dino = Dino(44,47)
        self.init_network()
        self.X = np.array([1.0, 1.0, 1.0, 1.0])
        self.action = 3

    def init_network(self):
        # TODO : find the appropriate number of nodes
        self.W1 = np.zeros((4, 3))
        self.W2 = np.zeros((3, 3))
        self.W3 = np.zeros((3 ,4))
        np_rand(self.W1, 4, 3)
        np_rand(self.W2, 3, 3)
        np_rand(self.W3, 3, 4)

        self.b1 = np.zeros((1, 3))
        self.b2 = np.zeros((1, 3))
        self.b3 = np.zeros((1, 4))
        np_rand(self.b1, 1, 3)
        np_rand(self.b2, 1, 3)
        np_rand(self.b3, 1, 4)

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
        
    def forward(self, c, p):
        self.get_enemy_pos(c, p)

        a1 = np.dot(self.X, self.W1) + self.b1
        z1 = ReLU(a1)
        a2 = np.dot(z1, self.W2) + self.b2
        z2 = ReLU(a2)
        a3 = np.dot(z2, self.W3) + self.b3
        y = identity_function(a3)

        self.action = np.argmax(y)
        

class Generation:
    def __init__(self, n):
        self.generation = 1
        self.num = n
        self.instance = []
        self.create_instance()
    
    def create_instance(self):
        for i in range(self.num):
            self.instance.append(Instance())

    def generation_end(self):
        for i in range(len(self.instance)):
            if self.instance[i].dino.isDead == False:
                return False
        return True

    def save_score(self):
        self.gene_score = []
        for i in range(len(self.instance)):
            self.gene_score.append(self.instance[i].dino.score)

    def selection(self):
        for i in range(int(len(self.instance) * 0.4)):
            index = self.gene_score.index(max(self.gene_score))
            self.new_instance.append(self.instance[index])
            del self.instance[index]
        # Issue : list range out error

        print(self.new_instance)

    def cross_over(self):
        pass

    def mutation(self):
        pass

    def new_generation(self):
        self.generation += 1
        self.new_instance = []
        self.save_score()
        
        self.selection()
        self.cross_over()
        self.mutation()
