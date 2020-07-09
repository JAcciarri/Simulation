# -*- coding: utf-8 -*-

from processes import arrive, depart, initialize, report, timing, update_time_stats
from operator import itemgetter


def run_queue_simulation(config, first):
    # Initialize Run
    model, results_time = itemgetter("model", "results_time")(initialize(config))
    if (first):
        # Run Information
        print("Single-server queuing system (M/M/1)")
        print("Mean interarrival time:", round(model["mean_interarrival"], 6), "minutes")
        print("Mean service time:", round(model["mean_service"], 6), "minutes")
        print("Number of customers:", round(model["num_delays_required"], 6), "\n")

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
        # Invoke the report generator and end the simulation
        report(results_time, model)
    return results_time
