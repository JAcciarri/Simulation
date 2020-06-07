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
from distributions import uniform, exponential, gamma
from tests import mean_test, std_deviation_test
from plots import *


# General parameters
total_numbers = int(float(input("How many pseudorandoms numbers do you want to analyze?: ")))  # example: 500
# save = {"mode": True, "route": "graphs/", "total": total_numbers } # If mode is False, the graphs won't be saved

# Uniform parameters
a = 5
b = 19
 
# Exponential parameters
alpha_exp = 3

# Gamma parameters
k = 10
alpha_gamma = 3


# Main
uniform_values = np.zeros(total_numbers)
exp_values = np.zeros(total_numbers)
gamma_values = np.zeros(total_numbers)

for i in range(total_numbers):
    uniform_values[i] = uniform(a, b)
    exp_values[i]     = exponential(1/alpha_exp)
    gamma_values[i]   = gamma(k, alpha_gamma)

# Show
print()
print('-----UNIFORM DISTRIBUTION------')
# print(total_numbers + pseudorandom numbers generated)
# print(uniform_values)
mean_test(uniform_values, (a+b)/2)
std_deviation_test(uniform_values, ((b-a)**2/12)**(1/2))
print()

print('-----EXPONENTIAL DISTRIBUTION------')
# print(total_numbers + pseudorandom numbers generated)
# print(exp_values)
mean_test(exp_values, 1/alpha_exp)
std_deviation_test(exp_values, (1/(alpha_exp**2))**(1/2))
print()

print('-----GAMMA DISTRIBUTION------')
# print(total_numbers + pseudorandom numbers generated)
# print(gamma_values)
mean_test(gamma_values, k/alpha_gamma)
std_deviation_test(gamma_values, (k/alpha_gamma**2)**(1/2))
print()
