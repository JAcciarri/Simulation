# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
from plots import cdf_plots


# A list of pseudorandom number passes the mean and deviation tests within an acceptance intervale
acceptance_margin = 0.15
acceptance_interval = [1 - acceptance_margin, 1 + acceptance_margin]

# Simulated vs Analytic Statistic Parameters Calculation - Mean Test and Variance Test
def statistics_parameters_test(numbers_list, real_parameter_result, parameter_name):
    if (parameter_name == "Mean"): simulated_result = np.mean(numbers_list)
    if (parameter_name == "Variance"): simulated_result = np.var(numbers_list)
    print(parameter_name + " value is", simulated_result)
    print("And it is expected to be", real_parameter_result)
    relation = simulated_result / real_parameter_result
    if (acceptance_interval[0] <= relation <= acceptance_interval[1]):
        print(parameter_name + " Test PASSED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    else:
        print(parameter_name + " Test REJECTED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    print()

# χ2 Test
def chi_squared_test(numbers_list, distribution_name):
    # Something
    if(distribution_name == 'uniform'):
        pass # I don't know yet
    elif(distribution_name == 'normal'):
        pass # I don't know yet
    elif(distribution_name == 'exponential'):
        pass # I don't know yet
    elif(distribution_name == 'gamma'):
        pass # I don't know yet
    elif(distribution_name == 'binomial'):
        pass # I don't know yet
    elif(distribution_name == 'pascal'):
        pass # I don't know yet
    elif(distribution_name == 'hypergeometric'):
        pass # I don't know yet
    elif(distribution_name == 'poisson'):
        pass # I don't know yet
    elif(distribution_name == 'empirical'):
        pass # I don't know yet
    # More things...

# Simulated vs Analytic Plot of the cumulative distribution functions
def cdf_comparative_test(numbers_list, distribution_name, scale_parameter):
    sim_x = np.sort(numbers_list)
    sim_y = np.arange(1, len(sim_x)+1) / len(sim_x)
    if(distribution_name == 'exponential'):
        rv = stats.expon(scale=scale_parameter)
    else:
        # Var = "You're an elementary school boy"
        exit()
    x = np.linspace(0, np.minimum(rv.dist.b, max(sim_x)))
    cdf_plots(x, rv.cdf(x), sim_x, sim_y)
