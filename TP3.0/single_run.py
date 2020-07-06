from initialize import initialize
from timing import timing
from update_stats import update_time_avg_stats
from arrive import arrive
from depart import depart
from report import report


def run_queue_simulation(model):
    # Main
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
        update_time_avg_stats(model)
        # Invoke the appropriate event function
        if next_event_type == "arrival":
            arrive(model)
        elif next_event_type == "departure":
            depart(model)
    # Invoke the report generator and end the simulation
    report(model)
