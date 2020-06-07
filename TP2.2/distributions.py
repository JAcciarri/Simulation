# -*- coding: utf-8 -*-

from numpy.random import random
from numpy import log as ln


# Uniform Distribution Generator
def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

# Exponential Distribution Generator
def exponential(ex):
    r = random()
    x = -ex * ln(r)
    return x

# Gamma Distribution Generator
def gamma(k, alpha):
    tr = 1
    for _ in range(k):
        r = random()
        tr = tr * r
    x = -ln(tr) / alpha
    return x

# Normal Distribution Generator
def normal(m, d):
    sum = 0
    for _ in range(0, 12):
        r = random()
        sum += r
    x = d * (sum - 6) + m
    return x

# Pascal (Negative Binomial) Distribution Generator
def pascal(k, p):
    tr = 1
    qr = ln(1-p)
    for _ in range(k):
        r = random()
        tr = tr * r
    x = ln(tr)/qr
    return x
