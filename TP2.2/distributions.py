# -*- coding: utf-8 -*-

from numpy.random import random
from numpy import log as ln

def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

def exponential(ex):
    r = random()
    x = -ex * ln(r)
    return x

def gamma(k, alpha):
    tr = 1
    for _ in range(k):
        r = random()
        tr = tr * r
    x = -ln(tr) / alpha
    return x
