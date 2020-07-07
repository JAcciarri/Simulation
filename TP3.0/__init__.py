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
    - plots:       Plotting functions with optional automatic save
"""


from queue import Queue
from single_run import run_queue_simulation
# from plots import *

# General Configurations
iterations = int(float(input("QUEUING SYSTEM\nHow many iterations do you want to simulate?: ")))  # example: 500 
# save = {"mode": False, "route": "graphs/", "total": iterations} # If mode is False, the graphs won't be saved # NOT IMPLEMENTED YET

# Model Parameters Definition
results = []
# queue_limit = 100 # NOT IMPLEMENTED YET
model = {
    "area_num_in_queue": 0.0,
    "area_server_status": 0.0,
    "mean_interarrival": 0.0,
    "mean_service": 0.0,
    "num_customers_delayed": 0,
    "num_delays_required": 0,
    "num_in_queue": 0,
    "server_busy": False,
    "time": 0.0,
    "time_arrival_queue": Queue(maxsize=0),
    "time_last_event": 0.0,
    "total_of_delays": 0.0,
    "event_list": {
        "arrival": 0.0,
        "departure": 0.0
    }
}

# Main
if __name__ == '__main__':
    for i in range(iterations):
        print("\nModel " + str(i+1) + ":")
        result = run_queue_simulation(model)
        results.append(result)
        # Other Runs with other configs...
    
    print((i+1), "iterations results:", results)
    # Graphs with results...
