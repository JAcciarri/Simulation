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
    - tests:        File with our randomization tests
    - plots:        File with our plotting and save functions
'''


# Important Parameters (Ask Input for some of them??)
queue_limit = 100
num_customers_delayed = 0
next_event_type = -1
mean_interarrival = 1
mean_service = 0.5 
num_delays_required = 1000
num_events = 2
# Add the other variables: num_in_queue, server_busy...


# Model Initialization
def initialize():
    time = 0.0 # Simulation Clock
    server_busy = False
    num_in_queue = 0
    time_last_event = 0.0
    # Statistical Counters
    num_customers_delayed = 0
    total_of_delays = 0.0
    area_num_in_queue = 0.0
    area_server_status = 0.0
    # Initialize event list
    time_next_event[1] = time + exponential(mean_interarrival)
    time_next_event[2] = 1.0e+30

# Some info...
def timing():
    pass

# Some info...
def arrive():
    pass

# Some info...
def depart():
    pass

# Some info...
def report():
    pass

# Some info...
def update_time_avg_stats():
    pass

# Some info...
def exponential(mean_interarrival):
    pass


# Main
print("Single-server queueing system")
print("Mean interarrival time:", mean_interarrival, "minutes")
print("Mean service time:", mean_service, "minutes")
print("Number of customers:", num_delays_required)

# Initialize the simulation
initialize()
# Run the simulation while more delays are still needed
while(num_customers_delayed < num_delays_required):
    # Determine the next event
    timing()
    # Update time-average statistical accumulators
    update_time_avg_stats()
    # Invoke the appropriate event function
    if (next_event_type == 1):
        arrive()
    elif (next_event_type == 2):
        depart()
# Invoke the report generator and end the simulation
report()
