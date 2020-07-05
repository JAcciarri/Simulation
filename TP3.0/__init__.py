# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP3.0 - Single-server Queue System/Queuing Model

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
    - Scypy:    Distributions like χ2
    - Pandas:   Series and DataFrame table for tests results' summaring

Other Files:
    - tests:        File with our randomization tests --> sacar??
    - plots:        File with our plotting and save functions
'''


import numpy as np

# Parameters Configuration
queue_limit = 100 # Ask Input??
save = {"mode": False, "route": "graphs/"} # If mode is False, the graphs won't be saved

# Model Parameters Definition
model = {
    "area_num_in_queue": 0.0,
    "area_server_status": 0.0,
    "mean_interarrival": 0.0,
    "mean_service": 0.0,
    "next_event_type": 0,
    "num_customers_delayed": 0,
    "num_delays_required": 0,
    "num_events": 0,
    "num_in_queue": 0,
    "server_busy": None,
    "time": 0.0,
    "time_arrival": np.zeros(queue_limit + 1),
    "time_last_event": np.zeros(3),
    "total_of_delays": 0.0
}

# Model Initialization
def initialize(model):
    model["mean_interarrival"] = 1.0
    model["mean_service"] = 0.5
    model["num_delays_required"] = 1000
    model["num_events"] = 2
    model["server_busy"] = False
    model["time"] = 0.0 # Simulation Clock
    # num_in_queue = 0
    # time_last_event = 0.0
    # next_event_type = -1
    # --Statistical Counters--
    # num_customers_delayed = 0
    # total_of_delays = 0.0
    # area_num_in_queue = 0.0
    # area_server_status = 0.0
    # --Initialize event list--
    time_next_event[0] = model["time"] + exponential(model["mean_interarrival"])
    time_next_event[1] = 1.0e+30

# Some info...
def timing(model):
    pass

# Some info...
def arrive(model):
    pass

# Some info...
def depart(model):
    pass

# Some info...
def report(model):
    pass

# Some info...
def update_time_avg_stats(model):
    pass

# Some info...
def exponential(mean_interarrival):
    pass


# Main
print("Single-server queueing system")
print("Mean interarrival time:", model["mean_interarrival"], "minutes")
print("Mean service time:", model["mean_service"], "minutes")
print("Number of customers:", model["num_delays_required"])

# Initialize the simulation
initialize(model)
# Run the simulation while more delays are still needed
while(model["num_customers_delayed"] < model["num_delays_required"]):
    # Determine the next event
    timing(model)
    # Update time-average statistical accumulators
    update_time_avg_stats(model)
    # Invoke the appropriate event function
    if (model["next_event_type"] == 1):
        arrive(model)
    elif (model["next_event_type"] == 2):
        depart(model)
# Invoke the report generator and end the simulation
report(model)
