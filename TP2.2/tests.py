# -*- coding: utf-8 -*-

import numpy as np


# A list of pseudorandom number passes the mean and deviation tests within an acceptance intervale
acceptance_margin = 0.2
acceptance_interval = [1 - acceptance_margin, 1 + acceptance_margin]


# Simulated vs Analytic Calculation of the Mean
def mean_test(numbers_list, real_parameters):
    simulated_mean_result = np.mean(numbers_list)
    real_mean_result = real_parameters
    print("Mean value is", simulated_mean_result)
    print("And it is expected to be", real_mean_result)
    relation = simulated_mean_result / real_mean_result
    if (relation >= acceptance_interval[0] and relation <= acceptance_interval[1]):
        print("Mean Test PASSED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    else:
        print("Mean Test REJECTED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    print()

# Simulated vs Analytic Calculation of the Standard Deviation
def std_deviation_test(numbers_list, real_parameters):
    simulated_deviation_result = np.std(numbers_list)
    real_deviation_result = real_parameters
    print("Deviation value is", simulated_deviation_result)
    print("And it is expected to be", real_deviation_result)
    relation = simulated_deviation_result / real_deviation_result
    if (relation >= acceptance_interval[0] and relation <= acceptance_interval[1]):
        print("Standard Deviation Test PASSED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    else:
        print("Standard Deviation Test REJECTED within the acceptance margin of " + str(acceptance_margin*100) + " %")
    print()

# χ2 Test
def chi_squared_test():
    pass
    # To-Do (?)

# Simulated vs Analytic Plot of the cumulative distribution functions
def cdf_comparative_test():
    pass
    # To-Do...
