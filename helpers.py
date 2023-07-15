from random import random
from math import sqrt

def random_between(min, max):
    return random() * (max - min) + min

def get_distance(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
