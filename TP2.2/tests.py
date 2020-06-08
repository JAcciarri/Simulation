# -*- coding: utf-8 -*-

import numpy as np


# A list of pseudorandom number passes the mean and deviation tests within an acceptance intervale
acceptance_margin = 0.15
acceptance_interval = [1 - acceptance_margin, 1 + acceptance_margin]

# Simulated vs Analytic Statistic Parameters Calculation - Mean Test and Variance Test
def statistics_parameters_test(numbers_list, real_parameters, statistic_parameter):
    if (statistic_parameter == "Mean"): simulated_result = np.mean(numbers_list)
    if (statistic_parameter == "Variance"): simulated_result = np.var(numbers_list)
    print(statistic_parameter + " value is", simulated_result)
    print("And it is expected to be", real_parameters)
    relation = simulated_result / real_parameters
    if (acceptance_interval[0] <= relation <= acceptance_interval[1]):
        print(statistic_parameter + " Test PASSED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    else:
        print(statistic_parameter + " Test REJECTED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    print()


# χ2 Test
def chi_squared_test():
    pass
    # To-Do (?)

# Simulated vs Analytic Plot of the cumulative distribution functions
def cdf_comparative_test():
    pass
    # To-Do...
