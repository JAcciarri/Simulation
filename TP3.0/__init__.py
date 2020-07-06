# -*- coding: utf-8 -*-

"""
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
"""


import numpy as np
from queue import Queue
from single_run import run_queue_simulation

# Model Parameters Definition
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

run_queue_simulation(model)
