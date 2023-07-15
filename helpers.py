from random import random
from math import sqrt

def randomBetween(min, max):
    return random() * (max - min) + min

def getDistance(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
