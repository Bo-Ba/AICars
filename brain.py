import math
import random
from random import gauss

import numpy as np
import numpy.random


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gauss(x, mutationRate):
    if random.random() * 10 < mutationRate:
        return x + random.gauss(0, 0.3)
    else:
        return x


gaussV = np.vectorize(gauss)


class Brain:
    test = 0

    def __init__(self, sizes):
        weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.hidden = weights[0].transpose()
        self.output = weights[1].transpose()
        self.biasHid = np.random.random(sizes[1])
        self.biasOut = np.random.random(sizes[2])

    def feedForward(self, data):
        data = np.asarray(data)
        hidden = data.dot(self.hidden)
        hidden += self.biasHid
        hidden = sigmoid(hidden)
        output = hidden.dot(self.output)
        output += self.biasOut
        return sigmoid(output)

    def mutate(self, mutationRate):
        self.hidden = np.array([gaussV(x, mutationRate) for x in self.hidden])
        self.output = np.array([gaussV(x, mutationRate) for x in self.output])
        self.biasOut = np.array([gaussV(x, mutationRate) for x in self.biasOut])
        self.biasHid = np.array([gaussV(x, mutationRate) for x in self.biasHid])
