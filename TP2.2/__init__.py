# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP2.2 - Pseudorandom Numbers Generation on Different Distributions

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 10/06/2020

Python Libraries/Modules Used:
    - Numpy:    Random Numbers, Functions and Array Manipulation
    - Pyplot:   Matplotlib Module for Graph Plotting
    - Seaborn:  Statistical and Scientific Graphs
    - Scypy:    Tests for Distributions like χ2

Other Files:
    - distributions: File with our analyzed distributions' definitions (and tests?)
    - tests:         File with our randomization tests for different distributions
    - plots:         File with our plotting and save functions
'''

import numpy as np
from distributions import uniform, exponential, gamma, normal, pascal, binomial
from tests import statistics_test
from plots import *

# General parameters
total_numbers = int(float(input("How many pseudorandom numbers would you want to analyze?: ")))  # example: 500
save = {"mode": False, "route": "graphs/", "total": total_numbers} # If mode is False, the graphs won't be saved

# Uniform parameters, U ~ (a: min, b: max)
a = 5
b = 19
 
# Exponential parameters, E ~ (alpha_exp: ?)
alpha_exp = 3

# Gamma parameters, G ~ (k: ?, alpha_gamma: ?)
k_gamma = 10
alpha_gamma = 3

# Normal parameters, N ~ (m: mean, d: deviation)
m = 10 
d = 2

# Binomial parameters, B ~ (n: amount of independent experiments, p: success probability)
n = 100
p = 0.5

# Pascal parameters, P ~ (r: success cases, p: success probability)
k_pascal = 4
p_pascal = 0.8


# Main
# Lists Initialization
uniform_values = np.zeros(total_numbers)
exp_values     = np.zeros(total_numbers)
gamma_values   = np.zeros(total_numbers)
normal_values  = np.zeros(total_numbers)
binomial_values  = np.zeros(total_numbers)
pascal_values  = np.zeros(total_numbers)

# Distributions Generation
for i in range(total_numbers):
    uniform_values[i] = uniform(a, b)
    exp_values[i]     = exponential(1/alpha_exp)
    gamma_values[i]   = gamma(k_gamma, alpha_gamma)
    normal_values[i]  = normal(m, d)
    binomial_values[i]  = binomial(n, p)
    pascal_values[i]  = pascal(k_pascal, p_pascal)

# Test & Show
print()
print('-----UNIFORM DISTRIBUTION------')
# print(total_numbers, "pseudorandom numbers generated")
# print(uniform_values)
statistics_test(uniform_values, (a+b)/2, 'Mean')
statistics_test(uniform_values, ((b-a)**2)/12, 'Variance')
print()

print('-----EXPONENTIAL DISTRIBUTION------')
# print(total_numbers, "pseudorandom numbers generated")
# print(exp_values)
statistics_test(exp_values, 1/alpha_exp, 'Mean')
statistics_test(exp_values, 1/(alpha_exp**2), 'Variance')
print()

print('-----GAMMA DISTRIBUTION------')
# print(total_numbers, "pseudorandom numbers generated")
# print(gamma_values)
statistics_test(gamma_values, k_gamma/alpha_gamma, 'Mean')
statistics_test(gamma_values, k_gamma/(alpha_gamma**2), 'Variance')
print()

print('-----NORMAL DISTRIBUTION------')
# print(total_numbers, "pseudorandom numbers generated")
# print(normal_values)
statistics_test(normal_values, m, 'Mean')
statistics_test(normal_values, d**2, 'Variance')
print()

print('-----NORMAL DISTRIBUTION------')
print(total_numbers, "pseudorandom numbers generated")
print(binomial_values)
statistics_test(binomial_values, n*p, 'Mean')
statistics_test(binomial_values, (n*p*(1-p)), 'Variance')
print()

print('-----PASCAL DISTRIBUTION------')
# print(total_numbers, "pseudorandom numbers generated")
# print(pascal_values)
statistics_test(pascal_values, (k_pascal*(1-p_pascal))/p_pascal, 'Mean')
statistics_test(pascal_values, ((k_pascal*(1-p_pascal))/p_pascal**2)**(1/2), 'Variance')
print()
