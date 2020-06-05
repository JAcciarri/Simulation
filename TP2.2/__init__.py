import numpy as np
from numpy.random import random
from math import log as ln

def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

def exponential(ex):
    r = random()
    x = -ex * ln(r)
    return x

iterations = 1000
a = 5
b = 19
alpha = 3
uniform_values = np.zeros(iterations)
exp_values = np.zeros(iterations)

for i in range(iterations):
    uniform_values[i] = uniform(a, b)
    exp_values[i] = exponential(1/alpha)


print()
print('-----UNIFORM VALUES------')
print(uniform_values)
print('Mean value is', np.mean(uniform_values))
print('and it is expected to be like', (a+b)/2)
print()

print('-----EXPONENTIAL VALUES------')
print(exp_values)
print('Mean value is', np.mean(exp_values))
print('and it is expected to be like', 1/(alpha))
print()