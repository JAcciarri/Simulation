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
    - processes:  Queuing model processes and random generator
    - plots:      Plotting functions with optional automatic save
"""


from queue import Queue
from processes import arrive, depart, initialize, report, timing, update_time_stats
# from plots import *

# General Configurations
# iterations = int(float(input("QUEUING SYSTEM M/M/1\nHow many iterations do you want to simulate?: ")))  # example: 500
# save = {"mode": False, "route": "graphs/", "total": iterations} # If mode is False, the graphs won't be saved

# Model Parameters Definition
# queue_limit = 100
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
    print("Single-server queueing system")
    print("Mean interarrival time:", model["mean_interarrival"], "minutes")
    print("Mean service time:", model["mean_service"], "minutes")
    print("Number of customers:", model["num_delays_required"])

    # Initialize the simulation
    initialize(model)
    # Run the simulation while more delays are still needed
    while model["num_customers_delayed"] < model["num_delays_required"]:
        # Determine the next event
        next_event_type, model["time"] = timing(model["event_list"])
        # Update time-average statistical accumulators
        update_time_stats(model)
        # Invoke the appropriate event function
        if next_event_type == "arrival":
            arrive(model)
        elif next_event_type == "departure":
            depart(model)
    print()
    # Invoke the report generator and end the simulation
    report(model)
