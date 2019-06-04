import numpy as np
import pygame as pg
import random
import copy
import pickle
from game import Dino

RAND_INIT = 5

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
    def __init__(self, dino=None):
        if dino == None:
            self.dino = Dino(44,47)
        else:
            self.dino = dino
        #Dino(44,47)
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

        self.network = [self.W1, self.W2, self.W3, self.b1, self.b2, self.b3]

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

    def print_network(self):
        print("W1")
        print(self.W1)
        print("W2")
        print(self.W2)
        print("W3")
        print(self.W3)
        print("b1")
        print(self.b1)
        print("b2")
        print(self.b2)
        print("b3")
        print(self.b3)
        print()
        
    def forward(self, c, p):
        self.get_enemy_pos(c, p)

        a1 = np.dot(self.X, self.W1) + self.b1
        z1 = ReLU(a1)
        a2 = np.dot(z1, self.W2) + self.b2
        z2 = ReLU(a2)
        a3 = np.dot(z2, self.W3) + self.b3
        y = identity_function(a3)

        self.action = np.argmax(y)

    def copy(self, new):
        new.W1 = copy.deepcopy(self.W1)
        new.W2 = copy.deepcopy(self.W2)
        new.W3 = copy.deepcopy(self.W3)

        new.b1 = copy.deepcopy(self.b1)
        new.b2 = copy.deepcopy(self.b2)
        new.b3 = copy.deepcopy(self.b3)

        self.network = [self.W1, self.W2, self.W3, self.b1, self.b2, self.b3]
        

class Generation:
    def __init__(self, n):
        self.generation = 1
        self.num = n
        self.instance = []
        self.gene_score = [0]
        self.create_instance()
    
    def create_instance(self):
        for i in range(self.num):
            self.instance.append(Instance())

    def generation_end(self):
        for i in range(self.num):
            if self.instance[i].dino.isDead == False:
                return False
        return True

    def save_score(self):
        self.gene_score = []
        for i in range(self.num):
            self.gene_score.append(self.instance[i].dino.score)

    def info(self):
        print("=============="+ "Generation "+ str(self.generation) + "==============")
        print("==========="+ "Best record "+ str(max(self.gene_score)) + "===========")
        print()

    def selection(self):
        for i in range(int(self.num * 0.4)):
            index = self.gene_score.index(max(self.gene_score))
            tmp = Instance()
            self.instance[index].copy(tmp)
            self.new_instance.append(tmp)
            
            del self.instance[index]
            del self.gene_score[index]

    def cross_over(self):
        count = 0
        for i in range(int(self.num * 0.2 / 2)):
            tmp1 = Instance()
            tmp2 = Instance()
            tmp1.print_network()
            self.new_instance[count].copy(tmp1)
            self.new_instance[count + 1].copy(tmp2)
            tmp1.print_network()
            for i in range(3):
                x = random.choice(tmp1.network)
                y = random.choice(tmp2.network)
                # swap
                z = x
                x = y
                y = z
                
            count += 2
            tmp1.print_network()
            self.new_instance.append(tmp1)
            self.new_instance.append(tmp2)

    def mutation(self):
        count = 0
        for i in range(int(self.num * 0.4)):
            tmp = Instance()
            self.new_instance[count].copy(tmp)
            
            for i in range(2):
                index = random.randrange(0, len(tmp.network))
                x = tmp.network[index]
                np_rand(x, x.shape[0], x.shape[1])
            self.new_instance.append(tmp)
            
    def new_generation(self):
        self.save_score()
        self.info()
        self.generation += 1
        self.new_instance = []
        self.selection()
        self.cross_over()
        self.mutation()
        self.instance = self.new_instance

class Save_Load:
    def __init__(self, g):
        self.g = g
        self.instance = []
        for i in range(g.num):
            self.instance.append(Instance(-1))
            
        
