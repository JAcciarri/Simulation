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

def gamma(k, alpha):
    tr = 1
    for _ in range(k):
        r = random()
        tr = tr * r
    x = -ln(tr) / alpha
    return x

# General parameters
iterations = 500

# Uniform parameters
a = 5
b = 19

# Exponential parameters
alpha_exp = 3

# Gamma parameters
k = 10
alpha_gamma = 3



# Main
uniform_values = np.zeros(iterations)
exp_values = np.zeros(iterations)
gamma_values = np.zeros(iterations)

for i in range(iterations):
    uniform_values[i] = uniform(a, b)
    exp_values[i] = exponential(1/alpha_exp)
    gamma_values[i] = gamma(k, alpha_gamma)

# Show
print()
print('-----UNIFORM VALUES------')
#print(uniform_values)
print('Mean value is', np.mean(uniform_values))
print('and it is expected to be like', (a+b)/2)
print()

print('-----EXPONENTIAL VALUES------')
#print(exp_values)
print('Mean value is', np.mean(exp_values))
print('and it is expected to be like', 1/alpha_exp)
print()

print('-----GAMMA VALUES------')
print(gamma_values)
print('Mean value is', np.mean(gamma_values))
print('and it is expected to be like', k/alpha_gamma)
print()