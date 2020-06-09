# -*- coding: utf-8 -*-

from numpy.random import random
from numpy import floor, log as ln, exp


# Uniform Distribution Generator
def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

# Normal Distribution Generator
def normal(m, d):
    sum = 0
    for _ in range(12):
        r = random()
        sum += r
    x = d * (sum - 6) + m
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

# Binomial Distribution Generator
def binomial(n, p):
    x = 0
    for _ in range(1, n):
        r = random()
        if (r - p <= 0):
            x += 1
    return x

# Pascal (Negative Binomial) Distribution Generator
def pascal(k, p):
    tr = 1
    qr = ln(1-p)
    for _ in range(k):
        r = random()
        tr = tr * r
    x = floor(ln(tr)/qr)
    return x

# Poisson Distribution Generator
def poisson(L):
    x = 0
    b = exp(-L)
    tr = 1
    while(tr-b >= 0):
        r = random()
        tr = tr * r
        x += 1
    return x
