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
from scipy import stats
from distributions import uniform, exponential, gamma, normal, pascal, binomial, poisson
from tests import statistics_parameters_test, cdf_comparative_test


# General parameters
iterations = int(float(input("How many pseudorandom numbers would you want to analyze?: ")))  # example: 500
save = {"mode": False, "route": "graphs/", "total": iterations} # If mode is False, the graphs won't be saved

# Uniform parameters, U ~ (a: min, b: max)
a = 5
b = 19

# Normal parameters, N ~ (m: mean, d: deviation)
m = 10 
d = 2

# Exponential parameters, E ~ (alpha_exp: rate parameter)
alpha_exp = 3

# Gamma parameters, G ~ (k: shape parameter, alpha_gamma: scale parameter)
k_gamma = 10
alpha_gamma = 3

# Binomial parameters, B ~ (n: amount of independent experiments, p: success probability)
n_binomial = 100
p_binomial = 0.5

# Pascal parameters, NB ~ (r: success cases, p: success probability)
k_pascal = 4
p_pascal = 0.8

# Poisson parameters, P ~ (L: rate parameter)
L = 10  # Lambda


# Main
# Lists Initialization
uniform_values   = np.zeros(iterations)
normal_values    = np.zeros(iterations)
exp_values       = np.zeros(iterations)
gamma_values     = np.zeros(iterations)
binomial_values  = np.zeros(iterations)
pascal_values    = np.zeros(iterations)
# hypergeometric_values = np.zeros(iterations)
poisson_values   = np.zeros(iterations)
# empirical = np.zeros(iterations)

# Distributions Generation
for i in range(iterations):
    uniform_values[i]   = uniform(a, b)
    normal_values[i]    = normal(m, d)
    exp_values[i]       = exponential(1/alpha_exp)
    gamma_values[i]     = gamma(k_gamma, alpha_gamma)
    binomial_values[i]  = binomial(n_binomial, p_binomial)
    pascal_values[i]    = pascal(k_pascal, p_pascal)
    poisson_values[i]   = poisson(L)

# Test & Show
print()
print('-----UNIFORM DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(uniform_values)
statistics_parameters_test(uniform_values, (a+b)/2, 'Mean')
statistics_parameters_test(uniform_values, ((b-a)**2)/12, 'Variance')
print()

print('-----NORMAL DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(normal_values)
statistics_parameters_test(normal_values, m, 'Mean')
statistics_parameters_test(normal_values, d**2, 'Variance')
print()

print('-----EXPONENTIAL DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(exp_values)
statistics_parameters_test(exp_values, 1/alpha_exp, 'Mean')
statistics_parameters_test(exp_values, 1/(alpha_exp**2), 'Variance')
cdf_comparative_test(exp_values) # TESTING... UNDER CONSTRUCTION
print()

print('-----GAMMA DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(gamma_values)
statistics_parameters_test(gamma_values, k_gamma/alpha_gamma, 'Mean')
statistics_parameters_test(gamma_values, k_gamma/(alpha_gamma**2), 'Variance')
print()

print('-----BINOMIAL DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(binomial_values)
statistics_parameters_test(binomial_values, n_binomial*p_binomial, 'Mean')
statistics_parameters_test(binomial_values, (n_binomial*p_binomial*(1-p_binomial)), 'Variance')
print()

print('-----PASCAL DISTRIBUTION (NEGATIVE BINOMIAL)------')
# print(iterations, "pseudorandom numbers generated")
# print(pascal_values)
statistics_parameters_test(pascal_values, (k_pascal*(1-p_pascal))/p_pascal, 'Mean')
statistics_parameters_test(pascal_values, ((k_pascal*(1-p_pascal))/p_pascal**2), 'Variance')
print()

print('-----POISSON DISTRIBUTION------')
# print(iterations, "pseudorandom numbers generated")
# print(poisson_values)
statistics_parameters_test(poisson_values, L, 'Mean')
statistics_parameters_test(poisson_values, L, 'Variance')
print()
