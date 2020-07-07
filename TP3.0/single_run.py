# -*- coding: utf-8 -*-

from processes import arrive, depart, initialize, report, timing, update_time_stats


def run_queue_simulation(model):
    # Specific Parameters
    model_config = {
        "mean_interarrival": 1.0,
        "mean_service": 0.5,
        "num_delays_required": 1000
    }

    # Initialize Run
    initialize(model, model_config)
    
    # Run Information
    print("Single-server queueing system (M/M/1)")
    print("Mean interarrival time:", model["mean_interarrival"], "minutes")
    print("Mean service time:", model["mean_service"], "minutes")
    print("Number of customers:", model["num_delays_required"])

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
    result = report(model)
    return result
