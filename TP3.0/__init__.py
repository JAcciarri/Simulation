# Constants
Q_LIMIT = 100
BUSY = 1
IDLE = 0

# Variables
num_custs_delayed = 0
next_event_type = -1
"""
num_events
num_in_q
server_status
"""
# Taken from "input file"
mean_interarrival = 1
mean_service = 0.5 
num_delays_required = 1000

# Functions

def initialize():
    return
def timing():
    return
def arrive():
    return
def depart():
    return
def report():
    return
def update_time_avg_stats():
    return
def expon(mean_interarrival):
    return


# Main
num_events = 2
print("Single-server queueing system")
print("Mean interrarival time", mean_interarrival, "minutes")
print("Mean service time", mean_service, "minutes")
print("Number of customers", num_delays_required)

# Initialize the simulation
initialize()
# Run the simulation while more delays are still needed
while(num_custs_delayed < num_delays_required):
    # Determine the next event
    timing()
    # Update time-average statistical accumulators
    update_time_avg_stats()
    #Invoke the appropriate event function
    if (next_event_type == 1):
        arrive()
    elif (next_event_type == 2):
        depart()
# Invoke the report generator and end the simulation
report()
