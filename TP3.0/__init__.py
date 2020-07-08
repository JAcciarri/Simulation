# -*- coding: utf-8 -*-

"""
UTN FRRO - Simulation 2020
TP3.0 - Single-server Queuing System

Authors:
    - Joshua Acciarri (44823)
    - Nicolás Antonelli (44852)
    - Alejandro Recalde (44704)

Professor: Torres, Juan
Final Date: 08/07/2020

Python Libraries/Modules Used:
    - Numpy:    Random Numbers and Array Manipulation
    - Pyplot:   Matplotlib Module for Graph Plotting
    - Seaborn:  Statistical and Scientific Graphs
    - Pandas:   Series and DataFrame tables

Other Files:
    - single_run:  Execution for every model configuration
    - processes:   Queuing model processes and random generator
    - utils:       Useful functions modularized in this file
    - plots:       Plotting functions with optional automatic save
"""

from single_run import run_queue_simulation
from plots import line_plot_stats
from utils import get_expected_values


# General Configuration
n_runs = 10 # Iterations
save = {"mode": False, "route": "graphs/", "total": n_runs} # If mode is False, the graphs won't be saved

# Model Parameters Definition
results = []
n_delays = 1000
configs = [
    {
        "arrival_rate": 0.5,
        "service_rate": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.25 * Service Rate
    {
        "arrival_rate": 1,
        "service_rate": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.5 * Service Rate
    {
        "arrival_rate": 1.5,
        "service_rate": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 0.75 * Service Rate
    {
        "arrival_rate": 2,
        "service_rate": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 1 * Service Rate
    {
        "arrival_rate": 2.5,
        "service_rate": 2,
        "num_delays_required": n_delays,
    },  # Arrival Rate = 1.25 * Service Rate
]
current_config = configs[3]


# Main
if __name__ == "__main__":
    for i in range(n_runs):
        print("\nModel " + str(i + 1) + ":")
        result = run_queue_simulation(current_config)
        results.append(result)
        # Other Runs with other configs...
    expected = get_expected_values(current_config)

    # print((i + 1), "iterations results:", results)
    # Graphs with results...
    line_plot_stats(results, expected, save)
